#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open("README.md") as fp:
    DESCRIPTION = fp.read()

setup(
    name="pymousebot",
    version="1.0.0",
    description=DESCRIPTION,
    license="GNU",
    author="Oaker Min",
    author_email="ominbruce@outlook.com",
    maintainer="Oaker Min",
    maintainer_email="ominbruce@outlook.com",
    url="https://github.com/brootware/PyMouseBot.git",
)
