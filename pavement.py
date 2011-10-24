# -*- coding: utf-8 -*-
"""pavement.py -- pavement for de-vice.

Copyright 2011 Plexical. See LICENCE for permissions.
"""
import os
import sys

from paver.easy import *
from paver.setuputils import setup

from device import meta

setup(
    name=meta.name,
    packages=('device'),
    version=meta.version,
    author='Jacob Oscarson',
    author_email='jacob@plexical.com',
    install_requires=open(os.path.join('deps',
                                       'install.txt')).readlines()
)

@task
def boot_dev():
    "Prepares a checked out directory for development"
    sys.path.insert(0, os.path.join('deps', 'virtualenv.zip'))
    import virtualenv
    virtualenv.create_environment('.')
    sh('./bin/pip install -r deps/install.txt')
    sh('./bin/pip install -r deps/developer.txt')

@task
def clean():
    path('bin').rmtree()
    path('lib').rmtree()
    path('include').rmtree()
