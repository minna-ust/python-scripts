import os
import re
import sys
import argparse
import glob
import fnmatch
import subprocess
from pprint import pprint

fileList = []

class TextSearch:
	def __init__(self, path, filename, string):
		self.path = path
		self.filename = filename
		self.string = string

	def file_search(self):
		print("********* in file_search")
		# print(self.path)
		# os.chdir(self.path);
		# for file in glob.glob("TISCam.cpp"):
		    # print(file)
                pattern = 'TISCam.cpp'

                for dName, sdName, fList in os.walk(self.path):
                        for fileName in fList:
                                if fnmatch.fnmatch(fileName, pattern):
                                        fileList.append(os.path.join(dName, fileName))
                # pprint(fileList)


                for file in fileList:
                        print(file)
                        # print(subprocess.Popen(['grep', "wml", "./grep.txt"], stdout=subprocess.PIPE, shell=True))
                        p = subprocess.Popen('grep -rni %s %s' % (self.string, file), stdout=subprocess.PIPE, shell=True)

                        for line in p.stdout:
                                sys.stdout.write(line)

if __name__ == '__main__':
	ts = TextSearch("./", "TISCam.cpp", "filename")
	ts.file_search()
