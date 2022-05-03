import setuptools
from pyntegrate import __version__ as __version__

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name=__version__.__title__,
    version=__version__.__version__,
    author=__version__.__author__,
    author_email=__version__.__author_email__,
    description=__version__.__description__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=__version__.__url__,
    download_url=__version__.__download_url__,
    project_urls=__version__.__project_urls__,
    classifiers=__version__.__classifiers__,
    keywords=__version__.__keywords__,
    scripts=['pyntegrate/pyarctan.py'],
    packages=setuptools.find_packages(),
    ext_modules=[setuptools.Extension("pyntegrate.arctan", ["pyntegrate/arctan.c"])],
    python_requires=">=3.7",
)
