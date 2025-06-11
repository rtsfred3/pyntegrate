try:
    import tomllib
except:
    import tomli as tomllib

with open("pyproject.toml", "rb") as f:
    data = tomllib.load(f)

__title__ = data['project']['name']
__description__ = data['project']['description']
__url__ = data['project']['urls']["Homepage"]
__download_url__ = data['project']['urls']["Homepage"]
__version__ = data['project']['version']
__author__ = data['project']['authors'][0]['name']
__author_email__ = data['project']['authors'][0]['email']
__project_urls__ = {
    'Bug Tracker': data['project']['urls']["Bug Tracker"],
    'Source Code': data['project']['urls']["Repository"],
}
__classifiers__ = data['project']['classifiers']
__keywords__ = ' '.join(data['project']['keywords'])
__license__ = data['project']['license']
