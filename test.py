import inference_realesrgan_blender

upscaler = inference_realesrgan_blender.RealESRGANerBlender()
print(upscaler.upsampler)
upscaler.upscale(
    input_path='small_image.png',
    save_path='upscaled_image.png'
)
