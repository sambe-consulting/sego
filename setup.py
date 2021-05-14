import pathlib
from setuptools import setup, find_packages
import os
import fnmatch
import sysconfig
from setuptools.command.build_py import build_py as _build_py
EXCLUDE_FILES = [
    "sego/tests/*"
]


# The directory containing this file
HERE = os.path.dirname(os.path.realpath(__file__))

# The text of the README file
with open(HERE + "/README.md", encoding='utf-8') as f:
    README = f.read()
with open(HERE + '/requirements.txt') as f:
    required = f.read().splitlines()
    setup(
        name="sego",
        version="0.1.0.9",
        description="A web and micro-service framework for data analysts",
        long_description_content_type="text/markdown",
        long_description=README,
        url="https://github.com/sambe-consulting/sego",
        author="Sambe Consulting",
        author_email="development@sambe.co.za",
        license="Apache License 2.0",
        classifiers=[
            "License :: OSI Approved :: Apache Software License",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.7",
        ],
        packages=find_packages(exclude=("sego/tests",)),
        include_package_data=True,
        install_requires=required,

    )
# This call to setup() does all the work
