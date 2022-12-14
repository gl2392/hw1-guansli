# Always prefer setuptools over distutils
from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# This call to setup() does all the work
setup(
    name="hw1-guansli",  #
    version="0.1.1",
    description="HWK1, how to make a python library.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gl2392/hw1-guansli",
    author="GuansLi",
    author_email="example@email.com", #
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent"
    ],
    packages=["api_key"],  # todo: main folder
    include_package_data=True,
    install_requires=["numpy",
                      "polygon-api-client",
                      "sqlalchemy",
                      "matplotlib",
                      "pandas"]
)
