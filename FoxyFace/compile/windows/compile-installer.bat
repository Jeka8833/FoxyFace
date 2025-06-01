REM Yes-yes, you'll have to change the path to 7zip, or live without archiving at the very end of operations.
set "zip="D:\Program Files\7-Zip\7z.exe""

python -m venv .venv
call .venv\Scripts\activate

python -m pip install --upgrade pip
pip install pyinstaller_versionfile

python extract_version.py ..\..\current_release.json VERSION.txt

pyivf-make_version --source-format yaml --metadata-source verison.yml --outfile FoxyFace.exe.rc

call .venv\Scripts\deactivate

call ..\..\.venv\Scripts\activate

rmdir /s /q pyinstaller
git clone https://github.com/pyinstaller/pyinstaller.git

cd pyinstaller\bootloader

python ./waf all --target-arch=64bit

cd ..

pip install -e .

cd ..\..\..

pyinstaller --add-data="Assets:Assets" --add-data="Baballonia\\src\\Baballonia\\faceModel.onnx:Baballonia\\src\\Baballonia\\" --noconfirm --icon="Assets\\icon.png" --hide-console="hide-early" --clean --version-file="compile\\windows\\FoxyFace.exe.rc" --distpath=compile\windows\dist --workpath=compile\windows\build --name FoxyFace Main.py

cd compile\windows

copy debug_start.bat dist\FoxyFace\

cd dist
del /f FoxyFace.zip
%zip% a -tzip -mx9 FoxyFace.zip FoxyFace

pause