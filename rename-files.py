import os
import argparse
import sys


filelist = "LiDAR_Q_192.168.1.3.txt"
filenames = []

def renameFiles(dir):

    with open(filelist, "r+") as f:
        f.seek(0)
        for filename in os.listdir(dir):
            filenames.append(filename)

        # sorted(filenames)
        filenames.sort()      # sort alphabetically
        print("filenames: ")
        print(filenames)
        for name in filenames:
            f.write(name + "\n")
        f.truncate()


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("dir", type=str)
    args = parser.parse_args()

    print("args: ", args.dir)
    renameFiles(args.dir)
