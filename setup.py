# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import os.path

readme = ''
here = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(here, 'README.rst')
if os.path.exists(readme_path):
    with open(readme_path, 'rb') as stream:
        readme = stream.read().decode('utf8')

setup(
    long_description=readme,
    name='completions',
    version='0.0.8',
    description='Shell completions made easy.',
    python_requires='==3.*,>=3.4.0',
    project_urls={
        "homepage": "https://github.com/pwwang/completions",
        "repository": "https://github.com/pwwang/completions"
    },
    author='pwwang',
    author_email='pwwang@pwwang.com',
    license='MIT',
    entry_points={"console_scripts": ["completions = completions:main"]},
    packages=['completions'],
    package_dir={"": "."},
    package_data={"completions": ["*.bak"]},
    install_requires=['pyparam', 'rich==6.*,>=6.0.0'],
)
