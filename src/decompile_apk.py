#!/usr/bin/python
#coding=utf-8

import sys
import commands

def open_classyshark(apkfile):
    if apkfile != "":
        print "java -jar ../plugins/classyshark/ClassyShark.jar -open %s"%apkfile
        commands.getstatusoutput("java -jar ../plugins/classyshark/ClassyShark.jar -open %s"%apkfile)
    else:
        commands.getstatusoutput("java -jar ../plugins/classyshark/ClassyShark.jar")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        open_classyshark(sys.argv[1])
    else:
        open_classyshark("")