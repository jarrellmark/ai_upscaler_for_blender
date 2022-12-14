import copy
from datetime import date, datetime
from pathlib import Path
import sys
import traceback

import bpy

bl_info = {
    "name": "AI Upscaler for Blender",
    "blender": (2, 93, 0)
}

ai_upscaler_properties = {
    'render_resolution_x': 480,
    'render_resolution_x': 270,
    'scale_factor': 4.0
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

        # Output image paths
        layout.label(text="Small Image:")
        layout.prop(context.scene, "small_image_file_location")
        layout.label(text="Upscaled Image:")
        layout.prop(context.scene, "upscaled_image_file_location")
        
        
class AiUpscalerRenderOperator(bpy.types.Operator):
    bl_idname = "object.ai_upscaler_render_button" # <- put this string in layout.operator()
    bl_label = "Render & Upscale"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
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
        original_sys_path = copy.deepcopy(sys.path)
        # Delete numpy from modules because sys.modules is loaded before sys.path
        # and Blender has numpy in sys.modules.
        original_numpy_modules = {}
        for key, value in list(sys.modules.items()):
            if key.startswith('numpy'):
                original_numpy_modules[key] = value
                del sys.modules[key]
        
        try:
            known_exception = False

            # Set render resolution
            context.scene.render.resolution_x = ai_upscaler_properties['render_resolution_x']
            context.scene.render.resolution_y = ai_upscaler_properties['render_resolution_y']
            context.scene.render.resolution_percentage = 100
            
            # Calculate paths
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
            small_image_path = str(new_path / "small_image.png")
            upscaled_image_path = str(new_path / "upscaled_image.png")
            
            # Set small image location
            context.scene.render.filepath = small_image_path
            
            # Render
            bpy.ops.render.render(write_still=True)

            # Upscale
            sys.path = [str(Path(__file__).parent / 'Real-ESRGAN' / 'site-packages')] + sys.path
            sys.path = [str(Path(__file__).parent)] + sys.path
            import inference_realesrgan_blender
            upscaler = inference_realesrgan_blender.RealESRGANerBlender()
            upscaler.upscale(
                input_path=small_image_path,
                save_path=upscaled_image_path,
                scale_factor=ai_upscaler_properties['scale_factor']
            )

            # Display paths
            context.scene.small_image_file_location = small_image_path
            context.scene.upscaled_image_file_location = upscaled_image_path
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
            sys.path = copy.deepcopy(original_sys_path)
            for key, value in list(sys.modules.items()):
                if key.startswith('numpy'):
                    del sys.modules[key]
            for key, value in original_numpy_modules.items():
                sys.modules[key] = value
        return {'FINISHED'}


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


def unregister():
    bpy.utils.unregister_class(AiUpscalerPanel)
    del bpy.types.Scene.ai_upscaler_upscaled_resolution_x
    del bpy.types.Scene.ai_upscaler_upscaled_resolution_y
    del bpy.types.Scene.ai_upscaler_scale_factor
    del bpy.types.Scene.small_image_file_location
    del bpy.types.Scene.upscaled_image_file_location
    
    bpy.utils.unregister_class(AiUpscalerRenderOperator)


if __name__ == "__main__":
    register()
