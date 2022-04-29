#!/bin/bash

clear && clear

# cd dist/
# rm *.whl
# rm *.tar.gz
# cd ..

# python3 setup.py sdist
# python3 setup.py bdist_wheel
python3 setup.py bdist_wheel --plat-name=manylinux1-i686
python3 setup.py bdist_wheel --plat-name=manylinux1-x86_64

python3 setup.py bdist_wheel --plat-name=manylinux2010-i686
python3 setup.py bdist_wheel --plat-name=manylinux2010-x86_64

python3 setup.py bdist_wheel --plat-name=manylinux2014-i686
python3 setup.py bdist_wheel --plat-name=manylinux2014-x86_64
python3 setup.py bdist_wheel --plat-name=manylinux2014-aarch64
python3 setup.py bdist_wheel --plat-name=manylinux2014-armv7l
python3 setup.py bdist_wheel --plat-name=manylinux2014-ppc64
python3 setup.py bdist_wheel --plat-name=manylinux2014-ppc64le
python3 setup.py bdist_wheel --plat-name=manylinux2014-s390x

python3 setup.py bdist_wheel --plat-name=win32
python3 setup.py bdist_wheel --plat-name=win-amd64

python3 setup.py bdist_wheel --plat-name=macosx_10_11_x86_64
