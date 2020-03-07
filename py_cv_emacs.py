import os
import re
import sys
import argparse
import glob
import fnmatch
import subprocess
from pprint import pprint

class Process:
    def __init__(self, filename):
        self.filename = filename
        self.paperOrg = "/Users/mingliangwang/reference/org/cv_jd.org"

    def process(self):
        print("filename: ", self.filename);
        orgfile = open(self.paperOrg, 'a+')

        text = "* [[cv:" + self.filename;
        orgfile.write(text)
        orgfile.write("]]")
        orgfile.write("\n")

        orgfile.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    args = parser.parse_args()

    p = Process(args.file)
    p.process()
    print("Done.")
