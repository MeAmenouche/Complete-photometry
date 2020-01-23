#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 14:11:02 2019

@author: melissa
"""

import os
import glob
#import numpy
#import yaml
from setuptools import setup, find_packages, Extension

# Package name
name = 'Cat_Extraction'

# Packages (subdirectories in sugar_analysis/)
packages = find_packages()

# Scripts (in scripts/)
scripts = glob.glob("scripts/*.py")

package_data = {}

setup(name=name,
      description=("To DO"),
      classifiers=["Topic :: Scientific :: Astronomy",
                   "Intended Audience :: Science/Research"],
      author="MAmenouche",
      packages=packages,
      scripts=scripts)