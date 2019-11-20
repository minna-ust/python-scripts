import os
import sys
import subprocess


if __name__ == '__main__':

    p1 = subprocess.Popen('exec ls -lt %s' % ("/tmp/"), shell=True)
