import os
import re
import sys
import argparse
import glob
import fnmatch
import subprocess
from pprint import pprint

class Process:
    def __init__(self, filename, csvFileName):
        self.filename = filename
        self.csvFileName = csvFileName
        self.word_dict = dict()
        self.word_dict["_angle_ST_SC.csv"] = "side truck and side cargotainer"
        self.word_dict["_angle_ST_XY.csv"] = "side truck and xy plane"
        self.word_dict["_angle_ST_XZ.csv"] = "side truck and xz plane"
        self.word_dict["_angle_ST_YZ.csv"] = "side truck and yz plane"

        self.word_dict["_angle_SC_XY.csv"] = "container_side and xy plane"
        self.word_dict["_angle_SC_XZ.csv"] = "container_side and xz plane"
        self.word_dict["_angle_SC_YZ.csv"] = "container_side and yz plane"

        self.word_dict["_inliers.csv"] = "Model inliers: "
        self.word_dict["_height.csv"] = "height : "
        self.word_dict["_ring0.csv"] = "ringindex : 0 "
        self.word_dict["_ring1.csv"] = "ringindex : 1 "
        self.word_dict["_ring2.csv"] = "ringindex : 2 "
        self.word_dict["_ring3.csv"] = "ringindex : 3 "
        self.word_dict["_ring4.csv"] = "ringindex : 4 "
        self.word_dict["_ring5.csv"] = "ringindex : 5 "
        self.word_dict["_ring6.csv"] = "ringindex : 6 "
        self.word_dict["_ring7.csv"] = "ringindex : 7 "

        self.word_dict["_meanX.csv"] = "meanX of roiCloud:"
        self.word_dict["_meanX_filter.csv"] = "moving-average filter of meanX:"

    def process(self):
        print("************ process file", self.filename)
        csvfilename = os.path.splitext(self.filename)[0] + self.csvFileName
        csvfile = open(csvfilename, 'w')

        print(self.word_dict[self.csvFileName])

        cmd = ['grep', '-rn']
        cmd.append((self.word_dict[self.csvFileName]))
        # cmd.append('"')
        cmd.append(self.filename)
        print("cmd: ", cmd)
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        for line in p.stdout:
            sys.stdout.write(line)
            csvfile.write(line)
        p.kill()


        # if (self.csvFileName == "_angle_ST_SC.csv"):
        #     cmd = ['grep', '-rn']
        #     cmd.append((self.word_dict[self.csvFileName]))
        #     # cmd.append('"')
        #     cmd.append(self.filename)
        #     print("cmd: ", cmd)
        #     p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        #     for line in p.stdout:
        #         sys.stdout.write(line)
        #         csvfile.write(line)
        #     p.kill()

        # if (self.csvFileName == "_angle_ST_XY.csv"):
        #     p = subprocess.Popen('exec grep -rn "side truck and xy plane" %s' % self.filename, stdout=subprocess.PIPE, shell=True)
        #     for line in p.stdout:
        #         sys.stdout.write(line)
        #         csvfile.write(line)


        # if (self.csvFileName == "_angle_ST_XZ.csv"):
        #     p = subprocess.Popen('exec grep -rn "side truck and xz plane" %s' % self.filename, stdout=subprocess.PIPE, shell=True)
        #     for line in p.stdout:
        #         sys.stdout.write(line)
        #         csvfile.write(line)
        #     p.kill()

        # if (self.csvFileName == "_angle_ST_YZ.csv"):
        #     p = subprocess.Popen('exec grep -rn "side truck and yz plane" %s' % self.filename, stdout=subprocess.PIPE, shell=True)
        #     for line in p.stdout:
        #         sys.stdout.write(line)
        #         csvfile.write(line)
        #     p.kill()

        # if (self.csvFileName == "_angle_SC_XY.csv"):
        #     p = subprocess.Popen('exec grep -rn "side cargotainer and xy plane" %s' % self.filename, stdout=subprocess.PIPE, shell=True)
        #     for line in p.stdout:
        #         sys.stdout.write(line)
        #         csvfile.write(line)
        #     p.kill()

        # if (self.csvFileName == "_angle_SC_XZ.csv"):
        #     p = subprocess.Popen('exec grep -rn "side cargotainer and xz plane" %s' % self.filename, stdout=subprocess.PIPE, shell=True)
        #     for line in p.stdout:
        #         sys.stdout.write(line)
        #         csvfile.write(line)
        #     p.kill()

        # if (self.csvFileName == "_angle_SC_YZ.csv"):
        #     p = subprocess.Popen('exec grep -rn "side cargotainer and yz plane" %s' % self.filename, stdout=subprocess.PIPE, shell=True)
        #     for line in p.stdout:
        #         sys.stdout.write(line)
        #         csvfile.write(line)
        #     p.kill()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    args = parser.parse_args()
    print(args.file)

    meanX = Process(args.file, "_meanX.csv")
    meanX.process()

    meanX_filter = Process(args.file, "_meanX_filter.csv")
    meanX_filter.process()
    # for i in range(8):
    #     print("i: ", i)
    #     ring0 = Process(args.file, "_ring" + str(i) + ".csv")
    #     ring0.process()

    # height = Process(args.file, "_height.csv")
    # height.process()
    # stsc = Process(args.file, "_angle_ST_SC.csv")
    # stsc.process()

    # stxy = Process(args.file, "_angle_ST_XY.csv")
    # stxy.process()

    # stxz = Process(args.file, "_angle_ST_XZ.csv")
    # stxz.process()

    # scxy = Process(args.file, "_angle_SC_XY.csv")
    # scxy.process()

    # scxz = Process(args.file, "_angle_SC_XZ.csv")
    # scxz.process()

    # inlier = Process(args.file, "_inliers.csv")
    # inlier.process()
