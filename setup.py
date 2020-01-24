#!/usr/bin/python
#Last-modified: 24 Jan 2020 12:25:48 PM

#         Module/Scripts Description
# 
# Copyright (c) 2019 The Unversity of Texas at Dallas
# 
# This code is free software; you can redistribute it and/or modify it
# under the terms of the BSD License (see the file COPYING included with
# the distribution).
# 
# @version: 2.0.0
# @design: Yong Chen <yongchen1@utdallas.edu>
# @implementation: Yunfei Wang <yfwang0405@gmail.com>
# @corresponding author:  Michael Q. Zhang <michael.zhang@utdallas.edu>

# ------------------------------------
# python modules
# ------------------------------------

import os,sys
from setuptools import setup, find_packages, Extension

# ------------------------------------
# constants
# ------------------------------------

# ------------------------------------
# Misc functions
# ------------------------------------

# ------------------------------------
# Classes
# ------------------------------------

# ------------------------------------
# Main
# ------------------------------------

if __name__ == '__main__':
    if float(sys.version[:3])<3.7:
        sys.stderr.write("CRITICAL: Python version must be 3.7 or greater!\n")
        sys.exit(1)

    # includepy = "%s/include/python%s" % (sys.prefix, sys.version[:3])
    with open("README.rst",'r') as fh:
        long_description = fh.read()
        idx = long_description.find('\n')
        description = long_description[:idx].rstrip()
    # ngsplot version
    with open('RELEASE','r') as fh:
        PROG, VERSION = fh.readlines()[0].rstrip().split()[:2]

    # Compile Kent lib
    if 'clean' in sys.argv:
        print >>sys.stderr, "Clean dist and egg info ..."
        os.system('if [ -d dist ]; then rm -rf dist; fi')
        os.system('if [ -f {0}.egg-info ]; then rm {0}.egg-info; fi'.format(PROG))
        os.system('if [ -d {0}.egg-info ]; then rm -rf {0}.egg-info; fi'.format(PROG))
    
    # install requirement
    install_requires = [ ["numpy >= 1.4.1"]]
    # Python 2.6 requires argparse
    if float(sys.version[:3]) == 2.6:
        install_requires.append(["argparse >= 1.2.1"])
    install_requires.append(["numpy >= 1.13.1",
                             "pandas >= 0.15.2",
                             "matplotlib >= 2.0.2",
                             "seaborn >= 0.7.1",
                             "pysam >= 0.11.2.2",
                             "scipy >= 0.19.1",
                             "statsmodels >=0.8.0"])
    setup(name=PROG,
          version=VERSION,
          author='Yunfei Wang',
          author_email='yfwang0405@gmail.com',
          url='https://github.com/tsznxx/{0}'.format(PROG),
          license="GNU General Public License (GPL)",
          keywords = "C3S",
          description = (description),
          long_description = long_description,
          package_dir={PROG:'src'},
          packages = [PROG],
          scripts=['bin/runC3S.py'],
          ext_modules=[],
          classifiers=['Environment :: Console',
                       'Development Status :: 3 - Alpha',
                       'Intended Audience :: Developers',
                       'License :: OSI Approved :: GNU General Public License (GPL)',
                       'License :: Free for non-commercial use',
                       'Operating System :: Unix',
                       'Programming Language :: Python :: 2.7',
                       'Topic :: Scientific/Engineering :: Bio-Informatics'],
          install_requires=install_requires)
