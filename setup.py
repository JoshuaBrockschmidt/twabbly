#!/usr/bin/env python3

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name = 'twabbly',
    version = '0.0.1',
    description = 'A Twitter bot that learns how to speak from users',
    author = 'Joshua Brockschmidt',
    author_email = 'JoshuaBrockschmidt@gmail.com',
    url = 'https://github.com/JoshuaBrockschmidt/twabbly',
    install_requires = ['tweepy>=3']
)
