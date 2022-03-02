#!/usr/bin/env python
from importlib.metadata import entry_points
from platform import platform


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="pymousebot",
    version="1.0.0",
    description="Python bot for mouse event simulation",
    license="GNU",
    author="Oaker Min",
    author_email="ominbruce@outlook.com",
    maintainer="Oaker Min",
    maintainer_email="ominbruce@outlook.com",
    url="https://github.com/brootware/PyMouseBot.git",
    packages=['src'],
    platforms='any',
    py_modules=['mousebot'],
    entry_points='''
    [console_scripts]
    mousebot=mousebot:main
    '''
)
