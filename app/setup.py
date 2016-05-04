#!/usr/bin/env python3

import os
import setuptools

name = os.environ['PACKAGE_NAME']
version = os.environ['PACKAGE_VERSION']

setuptools.setup(
    name=name,
    version=version,
    packages=setuptools.find_packages(),
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': ['{name}={name}.__main__:main'.format(name=name)]
    })
