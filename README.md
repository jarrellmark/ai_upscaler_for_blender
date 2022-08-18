AI Upscaler for Blender
=======================

Dramatically reduce render times using the [Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN) upscaler.

**Rendered in 5 mins with upscaling**

![Teaser Upscaled](/assets/teaser_upscaled.jpg)

**Rendered in 37 mins without upscaling**

![Teaser Full Render](/assets/teaser_full_render.jpg)

Install
-------

⬇️ Download Add-on.

**Blender 3.1 or newer**

* [Windows](https://github.com/jarrellmark/ai_upscaler_for_blender/releases/download/v1.0.0/ai_upscaler_for_blender-windows-blender31.zip)
* [macOS - Intel](https://github.com/jarrellmark/ai_upscaler_for_blender/releases/download/v1.0.0/ai_upscaler_for_blender-macos-x64-blender31.zip)
* [macOS - Apple Silicon](https://github.com/jarrellmark/ai_upscaler_for_blender/releases/download/v1.0.0/ai_upscaler_for_blender-macos-arm64-blender31.zip)
* [Linux](https://github.com/jarrellmark/ai_upscaler_for_blender/releases/download/v1.0.0/ai_upscaler_for_blender-linux-blender31.zip)

⬇️ Open Blender.

![Open Blender](/assets/Open_Blender.png)

⬇️ Click 'Edit' -> 'Preferences...'.

![Edit Preferences](/assets/Edit_Preferences.png)

⬇️ Click 'Add-ons' on the left.

![Addons](/assets/Addons.png)

⬇️ Click 'Install...' on the upper right.

![Install](/assets/Install.png)

⬇️ Navigate to the ai_upscaler_for_blender zip file and click 'Install Add-on'.

![Install Addon](/assets/Install_Addon.png)

⬇️ Wait a few minutes until Blender starts responding again. There's a lot of files to unzip.

![Wait](/assets/Not_Responding.png)

Use
---

⬇️ Click 'File' -> 'Save'.

![File Save](/assets/File_Save.png)

⬇️ Go to 'Output Properties' by clicking the printer icon on the left. Scroll down to AI Upscaler, Upscaler: Real-ESRGAN.

![Output Properties](/assets/Output_Properties.png)

⬇️ Set the Output Path to an existing folder, such as your 'Downloads' folder.

![Output Path](/assets/Output_Path.png)

⬇️ Set the upscaled resolution and scale factor. Upscaled resolution is the final resolution after upscaling. For example, with Upscaled Resolution of 1920x1080 and scale factor of 4, Blender will render at 480x270 (1920/4 by 1080/4). Real-ESRGAN will upscale the 480x270 image by a factor of 4 to 1920x1080 (480\*4 by 270\*4).

![Resolution Scale Factor](/assets/Resolution_And_Scale_Factor.png)

⬇️ Click 'Render & Upscale'. Blender will be unresponsive until the full process is finished. It will take a while but should be much faster than rendering at full resolution.

![Render And Upscale](/assets/Render_And_Upscale.png)

⬇️ Look at 'Upscaled Image'. The upscaled image will be saved there.

![Upscaled Image](/assets/Upscaled_Image.png)


License
-------

License does not cover anything in the `assets` folder.

### Main License

```
    AI Upscaler for Blender
    Copyright (C) 2022  Mark Jarrell

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with this program; if not, write to the Free Software Foundation, Inc.,
    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
```

### Dependencies

| Name                    | Version         | License                                            |
|-------------------------|-----------------|----------------------------------------------------|
| Blender (bpy)           | 2.93            | GPL-2.0-or-later                                   |
| Markdown                | 3.4.1           | BSD License                                        |
| MarkupSafe              | 2.1.1           | BSD License                                        |
| Pillow                  | 9.2.0           | Historical Permission Notice and Disclaimer (HPND) |
| PyWavelets              | 1.3.0           | MIT License                                        |
| PyYAML                  | 6.0             | MIT License                                        |
| Real-ESRGAN             | v0.2.5.0        | BSD-3-Clause                               |
| Werkzeug                | 2.2.2           | BSD License                                        |
| absl-py                 | 1.2.0           | Apache Software License                            |
| addict                  | 2.4.0           | MIT License                                        |
| basicsr                 | 1.4.1           | Apache Software License                            |
| boto3                   | 1.18.26         | Apache Software License                            |
| botocore                | 1.21.26         | Apache Software License                            |
| cachetools              | 5.2.0           | MIT License                                        |
| certifi                 | 2022.6.15       | Mozilla Public License 2.0 (MPL 2.0)               |
| charset-normalizer      | 2.1.0           | MIT License                                        |
| colorama                | 0.4.4           | BSD License                                        |
| cycler                  | 0.11.0          | BSD License                                        |
| facexlib                | 0.2.4           | Apache Software License                            |
| ffmpeg-normalize        | 1.22.7          | MIT License                                        |
| ffmpeg-progress-yield   | 0.2.0           | MIT License                                        |
| filterpy                | 1.4.5           | MIT License                                        |
| fonttools               | 4.34.4          | MIT License                                        |
| future                  | 0.18.2          | MIT License                                        |
| gfpgan                  | 1.3.4           | Apache Software License                            |
| google-auth             | 2.10.0          | Apache Software License                            |
| google-auth-oauthlib    | 0.4.6           | Apache Software License                            |
| grpcio                  | 1.47.0          | Apache Software License                            |
| idna                    | 3.3             | BSD License                                        |
| imageio                 | 2.21.1          | BSD License                                        |
| importlib-metadata      | 4.12.0          | Apache Software License                            |
| jmespath                | 0.10.0          | MIT License                                        |
| kiwisolver              | 1.4.4           | BSD License                                        |
| llvmlite                | 0.39.0          | BSD                                                |
| lmdb                    | 1.3.0           | OLDAP-2.8                                          |
| matplotlib              | 3.5.3           | Python Software Foundation License                 |
| networkx                | 2.8.5           | BSD License                                        |
| numba                   | 0.56.0          | BSD License                                        |
| numpy                   | 1.20.3          | BSD License                                        |
| oauthlib                | 3.2.0           | BSD License                                        |
| opencv-python           | 4.6.0.66        | MIT License                                        |
| packaging               | 21.3            | Apache Software License; BSD License               |
| protobuf                | 3.19.4          | 3-Clause BSD License                               |
| pyasn1                  | 0.4.8           | BSD License                                        |
| pyasn1-modules          | 0.2.8           | BSD License                                        |
| pyparsing               | 3.0.9           | MIT License                                        |
| python-dateutil         | 2.8.2           | Apache Software License; BSD License               |
| realesrgan              | 0.2.5.0         | Apache Software License                            |
| requests                | 2.28.1          | Apache Software License                            |
| requests-oauthlib       | 1.3.1           | BSD License                                        |
| rsa                     | 4.9             | Apache Software License                            |
| s3transfer              | 0.5.0           | Apache Software License                            |
| scikit-image            | 0.19.3          | BSD License                                        |
| scipy                   | 1.9.0           | BSD License                                        |
| six                     | 1.16.0          | MIT License                                        |
| tb-nightly              | 2.11.0a20220812 | Apache Software License                            |
| tensorboard-data-server | 0.6.1           | Apache Software License                            |
| tensorboard-plugin-wit  | 1.8.1           | Apache 2.0                                         |
| tifffile                | 2022.8.8        | BSD License                                        |
| torch                   | 1.12.1+cpu      | BSD License                                        |
| torchaudio              | 0.12.1+cpu      | BSD License                                        |
| torchvision             | 0.13.1+cpu      | BSD                                                |
| tqdm                    | 4.64.0          | MIT License; Mozilla Public License 2.0 (MPL 2.0)  |
| typing-extensions       | 4.3.0           | Python Software Foundation License                 |
| urllib3                 | 1.26.6          | MIT License                                        |
| yapf                    | 0.32.0          | Apache Software License                            |
| zipp                    | 3.8.1           | MIT License                                        |

Build Instructions (For Developers)
-----------------------------------

### Windows

* Download and install mamba from mambaforge
  * https://github.com/conda-forge/miniforge#mambaforge
* Download AI Upscaler for Blender
 * `> git clone https://github.com/jarrellmark/ai_upscaler_for_blender.git`
 * `> cd ai_upscaler_for_blender`
 * `> git checkout tags/v1.0.0 -b v1.0.0`
* Download Real-ESRGAN v0.2.5.0 (April 24, 2022)
  * Reference
    * https://github.com/xinntao/Real-ESRGAN
  * `> git clone https://github.com/xinntao/Real-ESRGAN.git`
  * `> cd Real-ESRGAN`
  * `> git checkout tags/v0.2.5.0 -b v0.2.5.0`
* Remove the conda environment if it already exists
  * `> mamba remove --name ai_upscaler_for_blender --all`
* Create initial conda environment
  * For Blender 2.93 LTS
    * `> mamba create --name ai_upscaler_for_blender python=3.9`
  * For Blender 3.1+
    * `> mamba create --name ai_upscaler_for_blender python=3.10`
  * `> mamba activate ai_upscaler_for_blender`
* Install PyTorch 1.12.1
  * Reference
    * https://pytorch.org/get-started/locally
    * Select Stable (1.12.1) / Windows / Pip / Python / CPU
  * `> pip3 install --target site-packages torch torchvision torchaudio`
  * `> pip3 install torch torchvision torchaudio`
* Install dependent packages
  * First comment out the following in requirements.txt
    * Original lines
      * ```
        facexlib>=0.2.0.3
        gfpgan>=0.2.1
        ```
    * After modifying requirements.txt
      * ```
        # facexlib>=0.2.0.3
        # gfpgan>=0.2.1
        ```
  * ```
    # Install basicsr - https://github.com/xinntao/BasicSR
    # We use BasicSR for both training and inference
    pip install --target site-packages basicsr
    # facexlib and gfpgan are for face enhancement
    ## pip install --target site-packages facexlib
    ## pip install --target site-packages gfpgan
    pip install --target site-packages -r requirements.txt
    ## python setup.py develop
    pip install --target site-packages .
    ```
* Download pre-trained models
  * `> wget https://github.com/xinntao/Real-ESRGAN/releases/download/v0.1.0/RealESRGAN_x4plus.pth -OutFile experiments\pretrained_models\RealESRGAN_x4plus.pth`
* Optional: Run example inference
  * Add to top of inference_realesrgan.py
    * ```
      import site
      site.addsitedir('site-packages')
      ```
  * `> python inference_realesrgan.py -n RealESRGAN_x4plus -i inputs --fp32 # --face_enhance`
    * [Note](https://github.com/xinntao/Real-ESRGAN/issues/306): add --fp32 for cpu
* Build Blender addon
  * `> cd ../..`
  * Copy ai_upscaler_for_blender to aufb to prevent too long file paths
    * `> Remove-Item aufb -Recurse`
    * `> cp -r ai_upscaler_for_blender aufb`
  * For Blender 2.93 LTS
    * `> Compress-Archive -Path aufb ai_upscaler_for_blender-windows-blender293.zip`
  * For Blender 3.1+
    * `> Compress-Archive -Path aufb ai_upscaler_for_blender-windows-blender231.zip`
  * Or use 7-Zip to create the .zip, it's faster.
* Optional: Examine licenses
  * Reference
    * https://github.com/raimon49/pip-licenses
  * First install all the pip packages into the conda environment. Run above pip commands without `--target site-packages`.
  * `> pip install pip-licenses`
  * `> pip-licenses --format=markdown`
  * `> pip-licenses --format=csv > licenses.csv`

### macOS

* Download and install mamba from mambaforge
  * https://github.com/conda-forge/miniforge#mambaforge
* Download AI Upscaler for Blender
 * `% git clone https://github.com/jarrellmark/ai_upscaler_for_blender.git`
 * `% cd ai_upscaler_for_blender`
 * `% git checkout tags/v1.0.0 -b v1.0.0`
* Download Real-ESRGAN v0.2.5.0 (April 24, 2022)
  * Reference
    * https://github.com/xinntao/Real-ESRGAN
  * `% git clone https://github.com/xinntao/Real-ESRGAN.git`
  * `% cd Real-ESRGAN`
  * `% git checkout tags/v0.2.5.0 -b v0.2.5.0`
* Remove the conda environment if it already exists
  * `% mamba remove --name ai_upscaler_for_blender --all`
* Create initial conda environment
  * For Blender 2.93 LTS
    * `% mamba create --name ai_upscaler_for_blender python=3.9 nomkl`
  * For Blender 3.1+
    * `% mamba create --name ai_upscaler_for_blender python=3.10 nomkl`
  * `% mamba activate ai_upscaler_for_blender`
* Install PyTorch 1.12.1
  * Reference
    * https://pytorch.org/get-started/locally
    * Select Stable (1.12.1) / Mac / Pip / Python / Default
  * `% pip3 install --target site-packages torch torchvision torchaudio`
  * `% pip3 install torch torchvision torchaudio`
* Install dependent packages
  * First comment out the following in requirements.txt
    * Original lines
      * ```
        facexlib>=0.2.0.3
        gfpgan>=0.2.1
        ```
    * After modifying requirements.txt
      * ```
        # facexlib>=0.2.0.3
        # gfpgan>=0.2.1
        ```
  * ```
    # Install basicsr - https://github.com/xinntao/BasicSR
    # We use BasicSR for both training and inference
    pip install --target site-packages basicsr
    # facexlib and gfpgan are for face enhancement
    ## pip install --target site-packages facexlib
    ## pip install --target site-packages gfpgan
    pip install --target site-packages -r requirements.txt
    ## python setup.py develop
    pip install --target site-packages .
    ```
* Download pre-trained models
  * `% curl -L -o experiments/pretrained_models/RealESRGAN_x4plus.pth https://github.com/xinntao/Real-ESRGAN/releases/download/v0.1.0/RealESRGAN_x4plus.pth`
* Optional: Run example inference
  * Add to top of inference_realesrgan.py
    * ```
      import site
      site.addsitedir('site-packages')
      ```
  * `% python inference_realesrgan.py -n RealESRGAN_x4plus -i inputs --fp32 # --face_enhance`
    * [Note](https://github.com/xinntao/Real-ESRGAN/issues/306): add --fp32 for cpu
* Build Blender addon
  * `% cd ../..`
  * For Blender 2.93 LTS
    * For macOS - Apple Silicon
      * `% zip -r ai_upscaler_for_blender-macos-arm64-blender293.zip ai_upscaler_for_blender`
    * For macOS - Intel
      * `% zip -r ai_upscaler_for_blender-macos-x64-blender293.zip ai_upscaler_for_blender`
  * For Blender 3.1+
    * For macOS - Apple Silicon
      * `% zip -r ai_upscaler_for_blender-macos-arm64-blender231.zip ai_upscaler_for_blender`
    * For macOS - Intel
      * `% zip -r ai_upscaler_for_blender-macos-x64-blender231.zip ai_upscaler_for_blender`
* Optional: Examine licenses
  * Reference
    * https://github.com/raimon49/pip-licenses
  * First install all the pip packages into the conda environment. Run above pip commands without `--target site-packages`.
  * `% pip install pip-licenses`
  * `% pip-licenses --format=markdown`
  * `% pip-licenses --format=csv > licenses.csv`

### Linux

* Download and install mamba from mambaforge
  * https://github.com/conda-forge/miniforge#mambaforge
* Download AI Upscaler for Blender
 * `$ git clone https://github.com/jarrellmark/ai_upscaler_for_blender.git`
 * `$ cd ai_upscaler_for_blender`
 * `$ git checkout tags/v1.0.0 -b v1.0.0`
* Download Real-ESRGAN v0.2.5.0 (April 24, 2022)
  * Reference
    * https://github.com/xinntao/Real-ESRGAN
  * `$ git clone https://github.com/xinntao/Real-ESRGAN.git`
  * `$ cd Real-ESRGAN`
  * `$ git checkout tags/v0.2.5.0 -b v0.2.5.0`
* Remove the conda environment if it already exists
  * `$ mamba remove --name ai_upscaler_for_blender --all`
* Create initial conda environment
  * For Blender 2.93 LTS
    * `$ mamba create --name ai_upscaler_for_blender python=3.9 nomkl`
  * For Blender 3.1+
    * `$ mamba create --name ai_upscaler_for_blender python=3.10 nomkl`
  * `$ mamba activate ai_upscaler_for_blender`
* Install PyTorch 1.12.1
  * Reference
    * https://pytorch.org/get-started/locally
    * Select Stable (1.12.1) / Linux / Pip / Python / CPU
  * `$ pip3 install --target site-packages torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cpu`
  * `$ pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cpu`
* Install dependent packages
  * First comment out the following in requirements.txt
    * Original lines
      * ```
        facexlib>=0.2.0.3
        gfpgan>=0.2.1
        ```
    * After modifying requirements.txt
      * ```
        # facexlib>=0.2.0.3
        # gfpgan>=0.2.1
        ```
  * ```
    # Install basicsr - https://github.com/xinntao/BasicSR
    # We use BasicSR for both training and inference
    pip install --target site-packages basicsr
    # facexlib and gfpgan are for face enhancement
    ## pip install --target site-packages facexlib
    ## pip install --target site-packages gfpgan
    pip install --target site-packages -r requirements.txt
    ## python setup.py develop
    pip install --target site-packages .
    ```
* Download pre-trained models
  * `$ wget https://github.com/xinntao/Real-ESRGAN/releases/download/v0.1.0/RealESRGAN_x4plus.pth -P experiments/pretrained_models`
* Optional: Run example inference
  * Add to top of inference_realesrgan.py
    * ```
      import site
      site.addsitedir('site-packages')
      ```
  * `$ python inference_realesrgan.py -n RealESRGAN_x4plus -i inputs --fp32 # --face_enhance`
    * [Note](https://github.com/xinntao/Real-ESRGAN/issues/306): add --fp32 for cpu
* Build Blender addon
  * `$ cd ../..`
  * For Blender 2.93 LTS
    * `$ zip -r ai_upscaler_for_blender-linux-blender293.zip ai_upscaler_for_blender`
  * For Blender 3.1+
    * `$ zip -r ai_upscaler_for_blender-linux-blender31.zip ai_upscaler_for_blender`
* Optional: Examine licenses
  * Reference
    * https://github.com/raimon49/pip-licenses
  * First install all the pip packages into the conda environment. Run above pip commands without `--target site-packages`.
  * `$ pip install pip-licenses`
  * `$ pip-licenses --format=markdown`
  * `$ pip-licenses --format=csv > licenses.csv`
