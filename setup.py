#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: BeYoung
# Date: 2023/6/12 23:29
# Software: PyCharm
from os.path import join, dirname

from setuptools import setup, find_packages

setup(
    name="snowflake-tool",
    version="1.1.0",
    author="novice2194",
    author_email="2194150786@qq.com",
    url="https://github.com/novice2194/snowflake-tool",
    license="MIT",
    packages=find_packages(),
    description="Simple snowflake id generator",
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    long_description_content_type="text/markdown",
    keywords=['python', 'snowflake', 'id generator'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
