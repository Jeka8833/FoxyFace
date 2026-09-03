<div align="center">
  <h1>FoxyFace</h1>
  <a href="https://pypi.org/project/foxyface">
    <img src="https://img.shields.io/pypi/pyversions/foxyface" />
  </a>
</div>

<br>

FoxyFace allows you to use your real face to control your avatar's face in VRChat using any camera that is connected to your computer. You can also use the camera of an Android device, iOS device or another computer, but this will require you to download additional programs, [here are instructions on how to do it](https://foxyface.jeka8833.pp.ua/docs/FoxyFace/connection/Using-another-device-as-a-camera).

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

<details>
  <summary><b>Pre-compiled Binaries (Windows)</b></summary>
  <br/>

  For Windows users, it is recommended to use the pre-compiled standalone executable from GitHub Releases:
  - **[Download Latest Release](https://github.com/Jeka8833/FoxyFace/releases)**
  <br/>
</details>

<details>
  <summary><b>Python Package (pip)</b></summary>
  <br/>

  If you want to install and run FoxyFace as a Python package, it is recommended to set up a virtual environment first. Select your operating system below:

  <details>
    <summary><b>Windows</b></summary>
    <br/>

#### 1. Create and Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

#### 2. Install and Run

```bash
pip install "foxyface[default]"
```

> **Note:** If you are running a Windows 10 version older than **10.0.19041 (20H1)**, you need to install the CPU-only version instead:
> ```bash
> pip install "foxyface[cpu]"
> ```

Run the application:
```bash
venv\Scripts\foxyface.exe
```
*(or just `foxyface` if the virtual environment is activated)*

  <br/>
  </details>

  <details>
    <summary><b>Linux</b></summary>
    <br/>

#### 1. Create and Activate Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

#### 2. Install

Choose the appropriate command based on your hardware/GPU:

* **NVIDIA:**
  ```bash
  pip install "foxyface[nvidia]" --extra-index-url https://download.pytorch.org/whl/cu126
  ```

* **AMD:**
  > ⚠️ You **must use Python 3.12**. All newer versions of Python will not work.
  ```bash
  pip install "foxyface[rocm]" --extra-index-url https://repo.radeon.com/rocm/manylinux/rocm-rel-6.4.4/
  ```

* **CPU only:**
  ```bash
  pip install "foxyface[cpu]"
  ```

#### 3. Run the application

```bash
venv/bin/foxyface
```
*(or just `foxyface` if the virtual environment is activated)*

  <br/>
  </details>

  <details>
    <summary><b>macOS</b></summary>
    <br/>

#### 1. Create and Activate Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

#### 2. Install and Run

```bash
pip install "foxyface[default]"
```

Run the application:
```bash
venv/bin/foxyface
```
*(or just `foxyface` if the virtual environment is activated)*

  </details>

  <br/>

</details>

<details>
  <summary><b>Development / From Source</b></summary>
  <br/>

  If you want to contribute or modify the source code:

#### 1. Clone the repository

Make sure to include submodules during cloning:
```bash
git clone --recurse-submodules https://github.com/Jeka8833/FoxyFace.git
cd FoxyFace/FoxyFace
```

#### 2. Set up a virtual environment

You can let your IDE (e.g., PyCharm, VS Code) automatically create and manage the virtual environment, or create one manually:

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

#### 3. Install in editable mode

```bash
pip install -e ".[default,build]"
```

</details>
