# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='pyliczba',
    version='1.0',
    description='Converts numerical values to Polish text',
    url='http://github.com/sq6jnx/pyliczba',
    author='Michał Sadowski',
    license='GNU LGPL',
    packages=['pyliczba'],
    install_requires=[
        'six',
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
    zip_safe=False,
)
