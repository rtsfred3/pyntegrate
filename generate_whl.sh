#!/bin/bash

clear && clear

python3 setup.py bdist_wheel --plat-name=manylinux1_x86_64
python3 setup.py bdist_wheel --plat-name=win32
