# FoxyFace

FoxyFace allows you to use your real face to control your avatar's face in VRChat using any camera that is connected to your computer. FoxyFace is a good starting point as it doesn't require you to invest any money.
<br/><br/>

## Step 0

1. Make sure you've installed [VRCFaceTracking](https://docs.vrcft.io).
2. Make sure you find an avatar that supports face tracking or head movement. You **won't be able** to check if it works without this/third-party module enabled. Here's a video tutorial: [link](https://youtu.be/aitYy5H9YTM)
3. The **most important step** is to make sure that you have enabled [OSC](https://docs.vrcft.io/docs/intro/getting-started#3%EF%B8%8F-enable-osc-in-vrchat) in the avatar settings and enabled tracking of individual parts of the face/head; by default, this is all turned off.
<br/><br/>

## Installation

1. Download [FoxyFace.zip](https://github.com/Jeka8833/FoxyFace/releases/latest/download/FoxyFace.zip) and [FoxyFaceVRCFTInterface.zip](https://github.com/Jeka8833/FoxyFace/releases/latest/download/FoxyFaceVRCFTInterface.zip).
2. Unzip FoxyFace.zip to wherever you like.
3. Start the FoxyFace.exe program from the archive you unzipped.
4. Start the VRCFaceTracking program.
5. Click the "Module Registry" tab.
6. Click on the "+" button.
7. Select the "FoxyFaceVRCFTInterface.zip" file you downloaded at the 1-st step.

> [!NOTE]
> This is a simplified instruction, a more complete instruction will be released in a while.

## Camera setup

Basic notes that may help you:
1. Try to keep the original aspect ratio of your image from the camera. If the aspect ratio is incorrect, your face will **not be recognized** or the mask (You can see the mask in the MediaPipe -> Preview) will **not be correctly applied** to your face.
2. If you have a weak computer and see that the FPS when tracking your face is low, reduce the resolution of the camera image. You can also disable the neural network from Project Babble if you don't need cheeks and tongue.
3. If you are far away from the camera, increase the output resolution of the image from your camera so that your face occupies at least 256 pixels in the image.
4. In low light, the neural network from Project Babble will have quite a bit of noise in the output.

> [!NOTE]
> This is a simplified instruction, a more complete instruction will be released in a while.

## Updating the Project Babble neural network

Necessary for better tracking of cheeks and tongue.

1. Download: [model.onnx]( https://raw.githubusercontent.com/Project-Babble/ProjectBabble/50d03cec35ac43b6fad7507c2dbbfc0e5012b70d/BabbleApp/Models/EFFB0E11BS128V7.5/onnx/model.onnx)
2. Start the FoxyFace program
3. Click on the Settings button in the Babble category
4. In the "Custom Babble Model Path:" section, select (Click the “...” button) the downloaded file from step 1.

> [!NOTE]
> This is a simplified instruction, a more complete instruction will be released in a while.

## Build

> [!NOTE]
> Simply cloning (`git clone`) without `--recurse-submodules` or downloading a Zip archive from GitHub **won't work** because the repository uses **submodules**!

### Build FoxyFace

Python version 3.12 is required. A newer version of Python is not supported. Older versions of Python have not been tested.

Automatically configuring the Python Virtual Environment doesn't happen in the IDE, but the basic plan consists of:
1. Cloning the repository using:
```
git clone --recurse-submodules https://github.com/Jeka8833/FoxyFace.git
```
2. Opening FoxyFace folder in IDE (PyCharm)
3. The PyCharm may try to create .venv on its own, but it will most likely do so with the wrong version of Python, you need to recreate .venv with Python 3.12.
4. Next, the PyCharm will prompt you to install the required libraries from the `requirements.txt` file, you agree to this.

This is quite a complicated process for beginners, if you know how to automate this, feel free to offer your thoughts.
<br/>

### Build FoxyFaceVRCFTInterface

Clone the project using internal IDE (JetBrains Rider, Visual Studio, ect...) tools, and select the project file FoxyFaceVRCFTInterface.sln. Then you click FoxyFaceVRCFTInterface -> Build in the IDE, and it creates a compiled module for you in the release directory.

Instructions on where to put the module and in general on developing modules for VRCFT can be found [here](https://docs.vrcft.io/docs/vrcft-software/vrcft-sdk/tracking-module).
<br/><br/>

## License

> [!NOTE]
> This repository contains 2 separate projects and which have different licenses.

FoxyFace code is licensed under [Apache License 2.0](https://github.com/Jeka8833/FoxyFace/blob/main/FoxyFace/LICENSE).

FoxyFace uses code from third-party developers under license:
1. License for Baballonia: [Apache License 2.0](https://github.com/Jeka8833/Baballonia-Copy/blob/main/LICENSE)
<br/>

FoxyFaceVRCFTInterface code is licensed under [Unlicense](https://github.com/Jeka8833/FoxyFace/blob/main/FoxyFaceVRCFTInterface/UNLICENSE).

FoxyFaceVRCFTInterface uses code from third-party developers under license:
1. License for VRCFaceTracking: [Apache License 2.0](https://github.com/benaclejames/VRCFaceTracking/blob/master/LICENSE)
