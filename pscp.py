import os
import sys
import subprocess
import argparse
import datetime
import time


if __name__ == '__main__':
    print(sys.argv[1])
    parser = argparse.ArgumentParser()
    parser.add_argument("src", type=str)
    # parser.add_argument("des")
    args = parser.parse_args()
    print(args.src)
    p = subprocess.Popen('exec scp -r %s wml@192.168.10.25:~/tmp/' % args.src, stdout=subprocess.PIPE, shell=True)
