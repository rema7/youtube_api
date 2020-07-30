from setuptools import setup, find_packages

requires = [
    'google-api-python-client>=1.10.0,<1.11.0',
    'dataclasses-json>=0.5.2',
]

setup(
    name='youtube-api',
    version='0.1.0',
    description='YouTube api',
    license='MIT',
    packages=find_packages(exclude=['tests*']),
    url='https://github.com/rema7/youtube_api',
    install_requires=requires
)
