#!/usr/bin/env python

import os
import re
import sys

from setuptools import setup
from setuptools.command.test import test as TestCommand


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

packages = [
    'openfoodfacts',
]

requires = [req for req in open('requirements.txt').read().split('\n') if req.strip()]
test_requirements = [req for req in open('requirements_test.txt').read().split('\n') if req.strip()]

with open('openfoodfacts/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Cannot find version information')

with open('README.rst', 'r') as f:
    readme = f.read()

setup(
    name='openfoodfacts',
    version=version,
    description='Easy querying of OpenFoodFacts.',
    long_description=readme,
    author='Pierre Slamich',
    author_email='pierre@openfoodfacts.org',
    url='http://openfoodfacts.org',
    packages=packages,
    package_data={'': ['LICENSE']},
    package_dir={'openfoodfacts': 'openfoodfacts'},
    include_package_data=True,
    install_requires=requires,
    license='Apache 2.0',
    zip_safe=False,
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English', 'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ),
    test_suite='tests',
    tests_require=test_requirements,
    extras_require={
    },
)
