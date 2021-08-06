'''from distutils.core import setup, Extension

extension_mod = Extension("arctan",
                          ["arctan.c"])

setup(name="arctan",
      version='1.2.0',
      description = 'This is an arctan package',
      author='Ryan Fredrickson',
      author_email='rtsfred3@gmail.com',
      url='https://github.com/rtsfred3/pyntegrate',
      ext_modules=[extension_mod])'''

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="arctan-rtsfred3",
    version="1.3.2",
    author="Ryan Fredrickson",
    author_email="rtsfred3@gmail.com",
    description="This is an arctan package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rtsfred3/pyntegrate",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: C",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    scripts=['pyntegrate/pyarctan.py'],
    packages=setuptools.find_packages(),
    ext_modules=[setuptools.Extension("pyntegrate.arctan", ["pyntegrate/arctan.c"])],
    python_requires=">=3.6",
)
