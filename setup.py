#!/usr/bin/env python

import io
import os
import sys
from shutil import rmtree
from setuptools import find_packages, setup, Command

VERSION = '0.1.0'

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.md')) as f:
    long_description = f.read()

class UploadCommand(Command):
    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds…')
            rmtree(os.path.join(here, 'dist'))
        except OSError:
            pass

        self.status('Building Source and Wheel (universal) distribution…')
        os.system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))

        self.status('Uploading the package to PyPI via Twine…')
        os.system('twine upload dist/*')

        self.status('Pushing git tags…')
        os.system('git tag v{0}'.format(VERSION))
        os.system('git push --tags')
        
        sys.exit()

setup(
    name='bst',
    version=VERSION,
    description='A binary search tree implemented for learning purposes.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Ryan Gilbert',
    author_email='ryangilbert7926@gmail.com',
    python_requires='>=3.6',
    url='https://github.com/rgilbert1/bst',
    py_modules=['bst'],
    include_package_data=True,
    license='MIT',
    cmdclass={
        'upload': UploadCommand,
    },
)
