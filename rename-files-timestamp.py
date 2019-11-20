import os
import argparse
import sys

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ int(text.split('_')[0]) ]

filelist = "LiDAR_Q_192.168.1.3.txt"
filenames = []

def renameFiles(dir):

    with open(filelist, "r+") as f:
        f.seek(0)
        timestamp = 0

        for filename in os.listdir(dir):
            if filename == "LiDAR_Q_192.168.1.3.txt":
                continue
            src = filename
            index = int(src[5:11])
            print("index: ", index)
            timestamp = index
            dst = str(index) + '_0000' + str(timestamp) + '.pcd'
            os.rename(src, dst)
            filenames.append(dst)


        # sorted(filenames)
        filenames.sort(key=natural_keys)      # sort alphabetically
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
