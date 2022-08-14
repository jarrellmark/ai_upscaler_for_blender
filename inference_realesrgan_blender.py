"""
Adapted from https://github.com/xinntao/Real-ESRGAN/blob/v0.2.5.0/inference_realesrgan.py
""" 

# import site
# site.addsitedir('Real-ESRGAN/site-packages')

import argparse
import copy
import cv2
import glob
import os
from pathlib import Path
from basicsr.archs.rrdbnet_arch import RRDBNet

from realesrgan import RealESRGANer
from realesrgan.archs.srvgg_arch import SRVGGNetCompact

class RealESRGANerBlender():
    def __init__(self):
        # determine models according to model names
        model_name = 'RealESRGAN_x4plus' # x4 RRDBNet model
        model = RRDBNet(num_in_ch=3, num_out_ch=3, num_feat=64, num_block=23, num_grow_ch=32, scale=4)
        netscale = 4

        # determine model paths
        model_path = str(Path(__file__).parent / "Real-ESRGAN/experiments/pretrained_models" / f"{model_name}.pth")
        if not os.path.isfile(model_path):
            model_path = str(Path(__file__).parent / "Real-ESRGAN/realesrgan/weights" / f"{model_name}.pth")
        if not os.path.isfile(model_path):
            raise ValueError(f'Model {model_name} does not exist at or {model_path}.')

        # restorer
        self.upsampler = RealESRGANer(
            scale=netscale,
            model_path=model_path,
            model=model,
            tile=0, # Tile size, 0 for no tile during testing
            tile_pad=10, # Tile padding
            pre_pad=0, # Pre padding size at each border
            half=False # Use fp32 precision during inference. Default: fp16 (half precision).
        )

    
    def upscale(self, input_path, save_path, scale_factor=4.0):
        img = cv2.imread(input_path, cv2.IMREAD_UNCHANGED)
        if len(img.shape) == 3 and img.shape[2] == 4:
            img_mode = 'RGBA'
        else:
            img_mode = None

        try:
            output, _ = self.upsampler.enhance(img, outscale=scale_factor)
        except RuntimeError as error:
            print('Error', error)
            print('If you encounter CUDA out of memory, try to set --tile with a smaller number.')
        else:
            extension = 'png'
            cv2.imwrite(save_path, output)


if __name__ == "__main__":
    upscaler = RealESRGANerBlender()
    print(upscaler.upsampler)
    upscaler.upscale(
        input_path='small_image.png',
        save_path='upscaled_image.png'
    )
