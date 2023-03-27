# Copyright (c) 2015 Fabian Kochem


try:
    from setuptools import setup, find_packages, Command
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages, Command

import platform
import os
import subprocess
import sys

from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)

setup(
    name='hug_store_redis',
    version='0.0.1',
    author='Fabian Kochem',
    author_email='fkochem@gmail.com',
    description='Redis Store extension for hug',
    url='https://github.com/vortec/hug_store_redis',

    # Dependencies
    install_requires=[
        'hug',
        'redis==4.5.3'
    ],
    tests_require=[
        'pytest==2.9.0'
    ],

    cmdclass={
        'test': PyTest
    },
    entry_points={},
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Database',
        'Topic :: Software Development :: Libraries'
    ],
)
