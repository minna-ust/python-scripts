import os
import re
import sys
import argparse
import glob
import fnmatch
import subprocess
from pprint import pprint
from pathlib import Path

if __name__ == '__main__':
    subprocess.Popen('exec touch tmpforebrowse.c', shell=True)
    subprocess.Popen('exec ebrowse tmpforebrowse.c', shell=True)
    for file in Path('./').rglob("./*.h"):
        # print(file)
        subprocess.Popen('exec ebrowse -a %s' % (file), shell=True)
    for file in Path('./').rglob("./*.hpp"):
        # print(file)
        subprocess.Popen('exec ebrowse -a %s' % (file), shell=True)

    for file in Path('./').rglob("./*.cpp"):
        # print(file)
        subprocess.Popen('exec ebrowse -a %s' % (file), shell=True)
    for file in Path('./').rglob("./*.c"):
        # print(file)
        subprocess.Popen('exec ebrowse -a %s' % (file), shell=True)
    for file in Path('./').rglob("./*.cc"):
        # print(file)
        subprocess.Popen('exec ebrowse -a %s' % (file), shell=True)
    print("ebrowse Done!")
