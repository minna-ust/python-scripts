import os
import sys
import subprocess
import argparse
import datetime
import time
import glob


if __name__ == '__main__':
    list_of_files = glob.glob('./*') # * means all
    p1 = subprocess.Popen('exec mkdir createdFilesFromLast5Hour', shell=True)
    time.sleep(0.3) # wait for finishing directory creating

    for file in list_of_files:
        # print("**1")
        # print(datetime.datetime.now().timestamp())
        # print("**2")
        # print(os.path.getctime(file))
        if ((datetime.datetime.now().timestamp() - os.path.getctime(file)) < 18000): # created from latest 5 hours
            print(file)
            p = subprocess.Popen('exec mv --verbose %s ./createdFilesFromLast5Hour' % (file), stdout=subprocess.PIPE, shell=True)
