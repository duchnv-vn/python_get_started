#!bin/sh

VERSION_NAME=python312

py -3.12 -m venv $VERSION_NAME && ./{$VERSION_NAME}/Scripts/activate

# cp -r ./$VERSION_NAME/* .

# rm -rf ./$VERSION_NAME


