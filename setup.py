#!/usr/bin/env python

from distutils.core import setup

setup(name='Lacquer',
    version='0.1',
    description='Thin layer of convenience on top of useful Python libraries.',
    author='Fernando Perez',
    url='http://github.com/fperez/lacquer',
    scripts=[
        './lacquer/rst2blog',
        './lacquer/latex2rst',
        ]
     )

