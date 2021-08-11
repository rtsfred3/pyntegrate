import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyntegrate",
    version="1.3.4b1",
    author="Ryan Fredrickson",
    author_email="rtsfred3@gmail.com",
    description="Pyntegrate is an example of various sorting algorithms using C Extensions.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rtsfred3/pyntegrate",
    download_url="https://pypi.org/project/pyntegrate/",
    project_urls={
            "Bug Tracker": "https://github.com/rtsfred3/pyntegrate/issues",
            "Source Code": "https://github.com/rtsfred3/pyntegrate",
        },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: C",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    scripts=['pyntegrate/pyarctan.py'],
    packages=setuptools.find_packages(),
    ext_modules=[setuptools.Extension("pyntegrate.arctan", ["pyntegrate/arctan.c"])],
    python_requires=">=3.6",
)
