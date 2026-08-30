REM Yes-yes, you'll have to change the path to 7zip, or live without archiving at the very end of operations.
set "zip="C:\Program Files\7-Zip\7z.exe""


REM =====================================
REM Convert program version
REM =====================================
rmdir /S /Q .venv
python -m venv .venv
call .venv\Scripts\activate

python -m pip install --upgrade pip
pip install pyinstaller_versionfile

python extract_version.py ..\..\current_release.json VERSION.txt

pyivf-make_version --source-format yaml --metadata-source verison.yml --outfile FoxyFace.exe.rc

call .venv\Scripts\deactivate



REM =====================================
REM Download pyinstaller
REM =====================================

rmdir /S /Q pyinstaller
git clone https://github.com/pyinstaller/pyinstaller.git


REM =====================================
REM Build GPU
REM =====================================
rmdir /S /Q .venv
python -m venv .venv
call .venv\Scripts\activate


cd pyinstaller\bootloader
python ./waf all --target-arch=64bit
cd ..
pip install -e .
cd ..

pip install -e ..\..\.

pyinstaller --noconfirm --icon="..\..\src\foxyface\assets\icon.png" --collect-all foxyface --hide-console="hide-early" --add-data "..\..\Baballonia\src\Baballonia\faceModel.onnx;foxyface\assets\baballonia" --hidden-import=mediapipe.tasks.c --add-data=".venv/Lib/site-packages/mediapipe/tasks/c;mediapipe/tasks/c"  --clean --version-file="FoxyFace.exe.rc" --distpath=distGPU --workpath=build --name FoxyFace Run.py



REM =====================================
REM Pack GPU build
REM =====================================

copy debug_start.bat distGPU\FoxyFace\

cd distGPU
del /f FoxyFace.zip
%zip% a -tzip -mx9 FoxyFace.zip FoxyFace
cd ..


REM =====================================
REM Build CPU
REM =====================================
rmdir /S /Q .venv
python -m venv .venv
call .venv\Scripts\activate


cd pyinstaller\bootloader
python ./waf all --target-arch=64bit
cd ..
pip install -e .
cd ..

pip install -e ..\..\.[cpu]

pyinstaller --noconfirm --icon="..\..\src\foxyface\assets\icon.png" --collect-all foxyface --hide-console="hide-early" --add-data "..\..\Baballonia\src\Baballonia\faceModel.onnx;foxyface\assets\baballonia" --hidden-import=mediapipe.tasks.c --add-data=".venv/Lib/site-packages/mediapipe/tasks/c;mediapipe/tasks/c"  --clean --version-file="FoxyFace.exe.rc" --distpath=distCPU --workpath=build --name FoxyFace Run.py



REM =====================================
REM Pack CPU build
REM =====================================

copy debug_start.bat distCPU\FoxyFace\

cd distCPU
del /f FoxyFace.zip
%zip% a -tzip -mx9 FoxyFace.zip FoxyFace

pause