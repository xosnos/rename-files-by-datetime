#!/usr/bin/env python3
"""
Module Docstring
"""
import os
import sys
import datetime

__author__ = "Steven Nguyen"
__version__ = "0.1.0"
__license__ = "MIT"

def getFileList(path):
    files = []
    for f in os.listdir(path):
        file = os.path.join(path, f)
        files.append(file)
    return files

def getFileDT(files):
    dates = []
    for f in files:
        dtm = os.path.getmtime(f)
        dtc = os.path.getctime(f)
        dt = dtm
        if dtc < dtm:
            dt = dtc
        data = datetime.datetime.fromtimestamp(dt)
        dates.append('{}-{}h{}m{}'.format(data.date(), data.hour, data.minute, data.second))
    return dates

def rename(path, files, dates):
    for i in range(len(files)):
        _, ext = os.path.splitext(files[i])
        name = os.path.join(path, dates[i] + ext)
        os.rename(files[i], name)

def main(args):
    """ Main entry point of the app """
    path = args[1]
    files = getFileList(path)
    dates = getFileDT(files)
    rename(path, files, dates)

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main(sys.argv)