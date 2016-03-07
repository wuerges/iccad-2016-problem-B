try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'ICCADVerify',
    'author': 'Emilio Wuerges',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'wuerges@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ICCADVerify'],
    'scripts': [],
    'name': 'ICCADVerify'
}

setup(**config)
