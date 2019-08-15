import os
import sys
import subprocess
import argparse
import datetime
import time


if __name__ == '__main__':
    print(sys.argv[1])
    parser = argparse.ArgumentParser()
    parser.add_argument("src", nargs='+')
    # parser.add_argument("des")
    args = parser.parse_args()
    print(args.src)
    # print(args.des)
    # print(os.getcwd())
    dir = datetime.datetime.now().strftime('%b-%d-%y_%H:%M:%S')
    # print(datetime.datetime.now())
    print("dir: ", dir)
    s1 = '/home/wml/Trash/'
    print("s1.join(dir)", s1 + dir)
    p1 = subprocess.Popen('exec mkdir %s' % (s1 + dir), shell=True)
    # p1.kill()
    time.sleep(0.5) # wait for finishing directory creating

    for item in args.src:
        p = subprocess.Popen('exec mv --verbose %s %s' % (item, s1 + dir + '/'), stdout=subprocess.PIPE, shell=True)
        for line in p.stdout:
            sys.stdout.write(line)
        p.kill()
