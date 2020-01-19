import os
import sys
import subprocess
import argparse
import datetime
import time
import glob


if __name__ == '__main__':
    list_of_files = glob.glob('/tmp/core*') # * means all if need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getctime)
    print("gdb mmCrane " + latest_file)

    # createdTime = time.localtime(os.stat(latest_file).st_ctime)
    # print(time.strftime('%H-%M-%S_%b-%d-%y', createdTime))
    # parser = argparse.ArgumentParser()
    # parser.add_argument("name", type=str)
    # # parser.add_argument("des")
    # args = parser.parse_args()
    # print(args.name)
    # # print(args.des)
    # # print(os.getcwd())
    # dir = datetime.datetime.now().strftime('%H-%M-%S_%b-%d-%y')
    # # print(datetime.datetime.now())
    # print("dir: ", dir)
    # # s1 = '/home/wml/Trash/'
    # # print("s1.join(dir)", s1 + dir)
    # p1 = subprocess.Popen('exec gdb mmCrane %s' % (latest_file), shell=True)
    # p1.kill()
    # time.sleep(0.5) # wait for finishing directory creating
