# -*- coding: utf-8 -*-
from distutils.core import setup

def readme():
    """Read README file and return its contents"""
    with open('README.md') as f:
        return f.read()

setup(
    name="namegenerator",
    description="Random name generator inspired by GitHub repository name suggestions",
    url="https://github.com/Skymirrh/glowing-hipster",
    version="0.2",
    author="Skymirrh",
    author_email="skymirrh@skymirrh.net",
    license="MIT",
    keywords="random name generator",
    packages=['namegenerator'],
    package_data={'namegenerator': ['lists/*', 'lists_sizes']},
    long_description=readme(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Topic :: Utilities",
        ],
)