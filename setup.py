#!/usr/bin/python
# coding=utf-8
"""****************************************************************************
Copyright (c) 2017 wntoolset

https://github.com/momoxie/wntoolset.git
****************************************************************************"""


import os
import sys
import fileinput
import shutil
import subprocess


def _check_python_version():
    major_ver = sys.version_info[0]
    if major_ver > 2:
        print ("The python version is %d.%d. But python 2.x is required. (Version 2.7 is well tested)\n"
               "Download it here: https://www.python.org/" % (major_ver, sys.version_info[1]))
        return False

    return True

def _install_dep_libs():
    print ("to do --> install dep libs")

if __name__ == '__main__':
    if not _check_python_version():
        exit()

    _install_dep_libs()
