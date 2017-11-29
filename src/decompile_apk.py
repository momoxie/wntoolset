#!/usr/bin/python
#coding=utf-8

import os,sys
import config_path

def open_classyshark(apkfile):
    if apkfile != "":
        print "java -jar %s/plugins/classyshark/ClassyShark.jar -open %s"%(config_path.g_project_dir,apkfile)
        os.system("java -jar %s/plugins/classyshark/ClassyShark.jar -open %s"%(config_path.g_project_dir,apkfile))
    else:
        os.system("java -jar %s/plugins/classyshark/ClassyShark.jar"%config_path.g_project_dir)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        open_classyshark(sys.argv[1])
    else:
        open_classyshark("")
