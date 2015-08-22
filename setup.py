# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    # Application name:
    name="hashable_collections",

    # Version number (initial):
    version="1.1",

    # Application author details:
    author="Akshat Mahajan",
    author_email="akshatm.bkk@gmail.com",

    # Packages
    packages=find_packages(),

    # Details
    url="http://akshatm.github.io/hashable_collections/",

    license="MIT",
    description="Hashable dictionaries and lists",

    classifiers = [
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Other Audience",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Software Development",
        "Topic :: Utilities"
        ],

    keywords = ["hash", "dictionary", "lists"],

    long_description=long_description
    )
