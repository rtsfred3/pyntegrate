from distutils.core import setup, Extension

extension_mod = Extension("arctan",
                          ["arctan.c"])

setup(name="arctan",
      version='1.1.9',
      description = 'This is an arctan package',
      ext_modules=[extension_mod])