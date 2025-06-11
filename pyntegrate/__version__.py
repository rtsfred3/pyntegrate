import pyntegrate.PyProjectDict as PyProjectDict

__title__ = PyProjectDict.PyProjectDict['project']['name']
__version__ = PyProjectDict.PyProjectDict['project']['version']
__description__ = PyProjectDict.PyProjectDict['project']['description']
__url__ = PyProjectDict.PyProjectDict['project']['urls']["Homepage"]
__download_url__ = PyProjectDict.PyProjectDict['project']['urls']["Homepage"]
__author__ = PyProjectDict.PyProjectDict['project']['authors'][0]['name']
__author_email__ = PyProjectDict.PyProjectDict['project']['authors'][0]['email']
__project_urls__ = {
    'Bug Tracker': PyProjectDict.PyProjectDict['project']['urls']["Bug Tracker"],
    'Source Code': PyProjectDict.PyProjectDict['project']['urls']["Repository"],
}
__classifiers__ = PyProjectDict.PyProjectDict['project']['classifiers']
__keywords__ = ' '.join(PyProjectDict.PyProjectDict['project']['keywords'])
__license__ = PyProjectDict.PyProjectDict['project']['license']
