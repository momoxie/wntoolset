#!/usr/bin/python
#coding=utf-8
import os,sys


#common config
def script_path():
    path = os.path.realpath(sys.path[0])
    if os.path.isfile(path):
        path = os.path.dirname(path)
    return os.path.abspath(path)

#py script path
g_pyscript_dir = script_path()
g_project_dir = os.path.join(g_pyscript_dir, "..")