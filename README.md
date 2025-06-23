# FoxyFace

FoxyFace allows you to use your real face to control your avatar's face in VRChat using any camera that is connected to your computer. You can also use the camera of an Android device, iOS device or another computer, but this will require you to download additional programs, [here are instructions on how to do it](https://github.com/Jeka8833/FoxyFace/wiki/Using-another-device-as-a-camera).

FoxyFace uses the [MediaPipe Face landmark detection](https://ai.google.dev/edge/mediapipe/solutions/vision/face_landmarker) neural network bundle and the neural network from [Project Babble](https://github.com/Project-Babble).

FoxyFace is a good starting point as it doesn't require you to invest any money if you have a computer and a camera on "any" of your devices.
<br/><br/>

## Almost complete facial tracking

![Example of Face Tracking](https://raw.githubusercontent.com/wiki/Jeka8833/FoxyFace/images/MainPage/Example.png)
<sub><sup>Face is taken from [FreePik](https://www.freepik.com/free-photo/medium-shot-woman-sticking-out-tongue_38162313.htm#fromView=keyword&amp;page=1&amp;position=45&amp;uuid=48e0b063-562f-4793-988c-3fb80cd0ca43&amp;query=Tongue+Out+Face), and [Yeenie](https://yoursmu.gumroad.com/l/yeenie) avatar is made by SMU</sup></sub>

The FoxyFace is currently tracking 83 parameters out of 102 parameters supported by VRCFT, which is 81%. That's taking into account the [Blended Shapes](https://docs.vrcft.io/docs/tutorial-avatars/tutorial-avatars-extras/unified-blendshapes).

<details>
  <summary>Supported parameters</summary>
  <br/>
  BrowInnerUpLeft, BrowInnerUpRight, BrowLowererLeft, BrowLowererRight, BrowOuterUpLeft, BrowOuterUpRight, BrowPinchLeft, BrowPinchRight, CheekPuffLeft, CheekPuffRight, CheekSquintLeft, CheekSquintRight, CheekSuckLeft, CheekSuckRight, EyeOpennessLeft, EyeOpennessRight, EyeSquintLeft, EyeSquintRight, EyeWideLeft, EyeWideRight, EyeXLeft, EyeXRight, EyeYLeft, EyeYRight, HeadPitch, HeadRoll, HeadX, HeadY, HeadYaw, HeadZ, JawForward, JawLeft, JawOpen, JawRight, LipFunnelLowerLeft, LipFunnelLowerRight, LipFunnelUpperLeft, LipFunnelUpperRight, LipPuckerLowerLeft, LipPuckerLowerRight, LipPuckerUpperLeft, LipPuckerUpperRight, LipSuckLowerLeft, LipSuckLowerRight, LipSuckUpperLeft, LipSuckUpperRight, MouthClosed, MouthCornerPullLeft, MouthCornerPullRight, MouthCornerSlantLeft, MouthCornerSlantRight, MouthDimpleLeft, MouthDimpleRight, MouthFrownLeft, MouthFrownRight, MouthLowerDownLeft, MouthLowerDownRight, MouthLowerLeft, MouthLowerRight, MouthPressLeft, MouthPressRight, MouthRaiserLower, MouthRaiserUpper, MouthStretchLeft, MouthStretchRight, MouthUpperLeft, MouthUpperRight, MouthUpperUpLeft, MouthUpperUpRight, NoseSneerLeft, NoseSneerRight, TongueBendDown, TongueCurlUp, TongueDown, TongueFlat, TongueLeft, TongueOut, TongueRight, TongueRoll, TongueSquish, TongueTwistLeft, TongueTwistRight, TongueUp
</details>

<details>
  <summary>Unsupported parameters</summary>
  <br/>
EyePupilDiameterMMLeft, EyePupilDiameterMMRight, JawBackward, JawClench, JawMandibleRaise, LipSuckCornerLeft, LipSuckCornerRight, MouthTightenerLeft, MouthTightenerRight, MouthUpperDeepenLeft, MouthUpperDeepenRight, NasalConstrictLeft, NasalConstrictRight, NasalDilationLeft, NasalDilationRight, NeckFlexLeft, NeckFlexRight, SoftPalateClose, ThroatSwallow
</details><br/>

## Step 0

1. Make sure you've installed [VRCFaceTracking](https://docs.vrcft.io).
2. Make sure you find an avatar that supports face tracking or head movement. You **won't be able** to check if it works without this/third-party module enabled. Here's a video tutorial: [link](https://youtu.be/aitYy5H9YTM)
3. The **most important step** is to make sure that you have enabled [OSC](https://docs.vrcft.io/docs/intro/getting-started#3%EF%B8%8F-enable-osc-in-vrchat) in the avatar settings and enabled tracking of individual parts of the face/head; by default, this is all turned off.
<br/>

## Installation

Perform the installation in this order:
1. Install FoxyFace, instructions [here](https://github.com/Jeka8833/FoxyFace/wiki/Install-FoxyFace).
2. Install FoxyFaceVRCFTInterface, instructions [here](https://github.com/Jeka8833/FoxyFace/wiki/Install-Module).
<br/>

## Camera setup

Instructions on how to set up the camera can be found [here](https://github.com/Jeka8833/FoxyFace/wiki/Camera-Settings).

Instructions on how to use another device as a webcam can be found [here](https://github.com/Jeka8833/FoxyFace/wiki/Using-another-device-as-a-camera).

<br/>

## Updating the Project Babble neural network

Instructions on how to update the neural network from Project Babble can be found [here](https://github.com/Jeka8833/FoxyFace/wiki/Update-Babble-Model).

<br/>

## Want to control your avatar's head rotation?

Instructions on how to track head rotation can be found [here](https://github.com/Jeka8833/FoxyFace/wiki/Head-Rotation).

<br/>

## Update FoxyFace Application

Instructions on how to update the FoxyFace app can be found [here](https://github.com/Jeka8833/FoxyFace/wiki/Update-FoxyFace).

<br/>

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
