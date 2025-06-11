# try:
#     import tomllib
# except:
#     import tomli as tomllib

import pyntegrate.PyProjectDict as PyProjectDict
import tomllib

with open("pyproject.toml", "rb") as f:
    data = tomllib.load(f)

__title__ = PyProjectDict.PyProjectDict['project']['name']
__version__ = PyProjectDict.PyProjectDict['project']['version']
__description__ = PyProjectDict.PyProjectDict['project']['description']
__url__ = data['project']['urls']["Homepage"]
__download_url__ = data['project']['urls']["Homepage"]
__author__ = PyProjectDict.PyProjectDict['project']['authors'][0]['name']
__author_email__ = PyProjectDict.PyProjectDict['project']['authors'][0]['email']
__project_urls__ = {
    'Bug Tracker': data['project']['urls']["Bug Tracker"],
    'Source Code': data['project']['urls']["Repository"],
}
__classifiers__ = PyProjectDict.PyProjectDict['project']['classifiers']
__keywords__ = ' '.join(PyProjectDict.PyProjectDict['project']['keywords'])
__license__ = PyProjectDict.PyProjectDict['project']['license']
