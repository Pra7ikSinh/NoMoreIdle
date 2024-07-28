#!/usr/bin/env python

from setuptools import setup

with open('requirements.txt') as f:
    install_requires = f.read().splitlines()

setup(
    name='no-more-idle',
    version='1.0.0',
    install_requires=install_requires,
    scripts=[
        'no-more-idle.py',
    ]
)