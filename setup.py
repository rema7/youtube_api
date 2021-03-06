from setuptools import find_packages
from setuptools import setup

requires = [
    'google-api-python-client>=1.10.0',
    'dataclasses-json>=0.5.2',
]

setup(
    name='youtubeapi',
    version='0.1.0',
    description='YouTube api',
    license='MIT',
    packages=find_packages(exclude=['tests*']),
    url='https://github.com/rema7/youtube_api',
    install_requires=requires
)
