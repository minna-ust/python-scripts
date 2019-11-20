import os
import sys
import subprocess
import argparse
import datetime
import time


if __name__ == '__main__':
    # print(sys.argv[1])

    parser = argparse.ArgumentParser()
    parser.add_argument("name", type=str)
    # parser.add_argument("des")
    args = parser.parse_args()
    print(args.name)
    # print(args.des)
    # print(os.getcwd())
    dir = datetime.datetime.now().strftime('%H-%M-%S_%b-%d-%y')
    # print(datetime.datetime.now())
    print("dir: ", dir)
    # print("s1.join(dir)", s1 + dir)
    p1 = subprocess.Popen('exec mkdir %s' % (args.name + '-' + dir), shell=True)
    # p1.kill()
    time.sleep(0.5) # wait for finishing directory creating
