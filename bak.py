import os
import re
import sys
import argparse
import glob
import fnmatch
import subprocess
from pprint import pprint


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("file", type=str)
    args = parser.parse_args()

    print("args: ", args.file)
    p = subprocess.Popen('cp -r %s %s' % (args.file, args.file + '.bak'), stdout=subprocess.PIPE, shell=True)

    for line in p.stdout:
        sys.stdout.write(line)
    print("Done.")
