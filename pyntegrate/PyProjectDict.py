import toml

PyProjectDict = {
    'build-system': {
        "requires": [ "flit_core >= 3.12.0, <4", "wheel" ],
        "build-backend": "flit_core.buildapi"
    },
    'project': {
        "name": "pyntegrate",
        "version": "1.3.7.dev11",
        "description": "Pyntegrate is an example of various sorting algorithms and other functions using C Extensions.",
        "readme": { "file": "README.md", "content-type": "text/markdown" },
        "authors": [
            { "name": "Ryan Fredrickson", "email": "rtsfred3+pyntegrate@gmail.com" }
        ],
        "keywords": [ 'pyntegrate', 'Python', 'C', 'CPython' ],
        "classifiers": [
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: Implementation :: CPython",
            "Programming Language :: C",
            "Operating System :: OS Independent"
        ],
        "license": "Apache-2.0",
        "requires-python": ">=3.7",
        "urls": {
            "Homepage": "https://github.com/rtsfred3/pyntegrate",
            "Repository": "https://github.com/rtsfred3/pyntegrate.git",
            "Bug Tracker": "https://github.com/rtsfred3/pyntegrate/issues"
        }
    }
}

def dump():
    with open('pyproject.toml', 'w') as f:
        toml.dump(PyProjectDict, f)

# try:
#     dump()
# except:
#     pass