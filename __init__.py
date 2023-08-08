import copy
from datetime import date, datetime
from pathlib import Path
import subprocess
import sys
import traceback

import bpy

bl_info = {
    "name": "AI Upscaler for Blender",
    "author": "jarrellmark",
    "version": (2, 0, 1),
    "blender": (3, 6, 0),
    "location": "Properties Editor > Output tab > AI Upscaler panel",
    "description": "Implementation of Real-ESRGAN upscaler to reduce render times by rendering at lower resolution and then upscaling.",
    "warning": "",
    "doc_url": "https://github.com/jarrellmark/ai_upscaler_for_blender",
    "tracker_url": "https://github.com/jarrellmark/ai_upscaler_for_blender/issues",
    "category": "Render",
}

ai_upscaler_properties = {
    'render_resolution_x': 480,
    'render_resolution_x': 270,
    'scale_factor': 4
}

def show_message_box(message="", title="AI Upscaler", icon='ERROR'):
    # Source: https://blender.stackexchange.com/questions/109711/how-to-popup-simple-message-box-from-python-console
    def draw(self, context):
        self.layout.label(text=message)

    bpy.context.window_manager.popup_menu(draw, title=title, icon=icon)

class AiUpscalerPanel(bpy.types.Panel):
    bl_label = "AI Upscaler"
    bl_idname = "OUTPUT_PT_ai_upscaler"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "output"

    def draw(self, context):
        layout = self.layout

        # Upscaler selection
        layout.label(text="Upscaler: Real-ESRGAN")

        # Output path
        layout.label(text="Output Path:")
        layout.label(text="    Must be a folder.")
        layout.label(text="    Folder must already exist.")
        layout.prop(context.scene.render, "filepath")
        
        # Upscaled Resolution
        layout.prop(context.scene, "ai_upscaler_upscaled_resolution_x")
        layout.prop(context.scene, "ai_upscaler_upscaled_resolution_y")
                
        # Scale Factor
        layout.label(text="Scale Factor:")
        layout.label(text="    2: Slower, Higher Quality")
        layout.label(text="    4: Faster, Lower Quality")
        layout.prop(context.scene, "ai_upscaler_scale_factor")
        ai_upscaler_properties['scale_factor'] = context.scene.ai_upscaler_scale_factor
        
        # Render Resolutionai_upscaler_scale_factor
        upscaled_resolution_x = context.scene.ai_upscaler_upscaled_resolution_x
        upscaled_resolution_y = context.scene.ai_upscaler_upscaled_resolution_y
        ai_upscaler_properties['render_resolution_x'] = int(round(upscaled_resolution_x * (1.0 / context.scene.ai_upscaler_scale_factor)))
        ai_upscaler_properties['render_resolution_y'] = int(round(upscaled_resolution_y * (1.0 / context.scene.ai_upscaler_scale_factor)))
        layout.label(text=f"Render Resolution: {ai_upscaler_properties['render_resolution_x']}x{ai_upscaler_properties['render_resolution_y']}")
        
        # Big render button
        row = layout.row()
        row.scale_y = 3.0
        row.operator("object.ai_upscaler_render_button")

        # Big render animation button
        row = layout.row()
        row.scale_y = 3.0
        row.operator("object.ai_upscaler_render_animation_button")

        # Output image paths
        layout.label(text="Small Image:")
        layout.prop(context.scene, "small_image_file_location")
        layout.label(text="Upscaled Image:")
        layout.prop(context.scene, "upscaled_image_file_location")
        

def render_execute(context, animation=False):
    # context.scene.ai_upscaler_scale_factor = 5
        
    # Save file to prevent losing data
    try:
        bpy.ops.wm.save_mainfile()
    except Exception as exception:
        show_message_box("Do 'File -> Save' and try again.")
        return {'FINISHED'}
    
    # Save variables to restore them later
    original_x = context.scene.render.resolution_x
    original_y = context.scene.render.resolution_y
    original_scale = context.scene.render.resolution_percentage
    original_render_path = context.scene.render.filepath
    
    try:
        known_exception = False

        # Set render resolution
        context.scene.render.resolution_x = ai_upscaler_properties['render_resolution_x']
        context.scene.render.resolution_y = ai_upscaler_properties['render_resolution_y']
        context.scene.render.resolution_percentage = 100
        
        # Set paths
        new_path = Path(context.scene.render.filepath)
        if not new_path.exists():
            show_message_box("Set 'Output Path' to an existing folder.")
            known_exception = True
            raise Exception("Set 'Output Path' to an existing folder.")
        if not new_path.is_dir():
            show_message_box("Set 'Output Path' to an existing folder.")
            known_exception = True
            raise Exception("Set 'Output Path' to an existing folder.")
        new_path = new_path / f"blender_output_{datetime.now().isoformat().replace(':', '-')}Z"
        small_images_path = new_path / "small_images"
        small_images_path.mkdir(parents=True, exist_ok=True)
        upscaled_images_path = new_path / "upscaled_images"
        upscaled_images_path.mkdir(parents=True, exist_ok=True)

        # Set upcaler paths
        if sys.platform.startswith('win32'):
            realesrgan_binary_path = Path(__file__).parent / 'realesrgan-ncnn-vulkan' / 'realesrgan-ncnn-vulkan-v0.2.0-windows' / 'realesrgan-ncnn-vulkan.exe'
        elif sys.platform.startswith('darwin'):
            realesrgan_binary_path = Path(__file__).parent / 'realesrgan-ncnn-vulkan' / 'realesrgan-ncnn-vulkan-v0.2.0-macos' / 'realesrgan-ncnn-vulkan'
        elif sys.platform.startswith('linux'):
            realesrgan_binary_path = Path(__file__).parent / 'realesrgan-ncnn-vulkan' / 'realesrgan-ncnn-vulkan-v0.2.0-ubuntu' / 'realesrgan-ncnn-vulkan'
        else:
            known_exception = True
            raise Exception(f"Unsupported platform: {sys.platform}")
        models_path = Path(__file__).parent / 'realesrgan-ncnn-vulkan' / 'models'
        
        # Render
        if not animation:
            context.scene.render.filepath = f"{small_images_path}/001.png"
            bpy.ops.render.render(write_still=True, animation=animation)
        else:
            context.scene.render.filepath = f"{small_images_path}/"
            bpy.ops.render.render(animation=animation)

        # Upscale
        for small_image_path in small_images_path.glob('*'):
            subprocess.run(
                [
                    str(realesrgan_binary_path.resolve()),
                    "-i", str(small_image_path.resolve()),
                    "-o", str((upscaled_images_path / small_image_path.name).resolve()),
                    "-s", str(ai_upscaler_properties['scale_factor']),
                    # "-t", "32",
                    "-m", str(models_path.resolve()),
                    "-n", "realesrgan-x4plus"
                ],
                check=True
            )

        # Display paths
        context.scene.small_image_file_location = str(small_images_path)
        context.scene.upscaled_image_file_location = str(upscaled_images_path)
    except Exception as exception:
        print(f"Exception:")
        print(traceback.format_exc())
        if not known_exception:
            show_message_box(traceback.format_exc())
    finally:
        # Restore original variables
        context.scene.render.resolution_x = original_x
        context.scene.render.resolution_y = original_y
        context.scene.render.resolution_percentage = original_scale
        context.scene.render.filepath = original_render_path
    return {'FINISHED'}


class AiUpscalerRenderOperator(bpy.types.Operator):
    bl_idname = "object.ai_upscaler_render_button"
    bl_label = "Render Image & Upscale"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        return render_execute(context, animation=False)


class AiUpscalerRenderAnimationOperator(bpy.types.Operator):
    bl_idname = "object.ai_upscaler_render_animation_button"
    bl_label = "Render Animation & Upscale"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        return render_execute(context, animation=True)


def register():
    bpy.utils.register_class(AiUpscalerPanel)
    bpy.types.Scene.ai_upscaler_upscaled_resolution_x = bpy.props.IntProperty(
        name="Upscaled Resolution X",
        default=1920,
        min=1
    )
    bpy.types.Scene.ai_upscaler_upscaled_resolution_y = bpy.props.IntProperty(
        name="Upscaled Resolution Y",
        default=1080,
        min=1
    )
    bpy.types.Scene.ai_upscaler_scale_factor = bpy.props.IntProperty(
        name="Scale Factor",
        default=4,
        min=2
    )
    bpy.types.Scene.small_image_file_location = bpy.props.StringProperty(
        name="File",
        default="",
        maxlen=1024
    )
    bpy.types.Scene.upscaled_image_file_location = bpy.props.StringProperty(
        name="File",
        default="",
        maxlen=1024
    )
    
    bpy.utils.register_class(AiUpscalerRenderOperator)
    bpy.utils.register_class(AiUpscalerRenderAnimationOperator)


def unregister():
    bpy.utils.unregister_class(AiUpscalerPanel)
    del bpy.types.Scene.ai_upscaler_upscaled_resolution_x
    del bpy.types.Scene.ai_upscaler_upscaled_resolution_y
    del bpy.types.Scene.ai_upscaler_scale_factor
    del bpy.types.Scene.small_image_file_location
    del bpy.types.Scene.upscaled_image_file_location
    
    bpy.utils.unregister_class(AiUpscalerRenderOperator)
    bpy.utils.unregister_class(AiUpscalerRenderAnimationOperator)


if __name__ == "__main__":
    register()
