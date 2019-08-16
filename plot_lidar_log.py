import matplotlib.pyplot as plt
import csv
import os
import argparse
import fnmatch
import sys

x = []
y = []
fileList = []

class PlotCSV:
    def __init__(self, pattern):
        self.pattern = pattern
        self.path = './'

    def plotCSV(self):
        for dName, sdName, fList in os.walk(self.path):
            for fileName in fList:
                if fnmatch.fnmatch(fileName, self.pattern):
                    fileList.append(os.path.join(dName, fileName))

        for file in fileList:
            plt.figure()
            print(file)
            with open(file, 'r') as csvfile:
                plots = csv.reader(csvfile, delimiter=' ')
                y = []
                for row in plots:
                    y.append(row[-1])
                plt.title(file)
                plt.plot(y, label=file)
                # plt.show()
        plt.show()


# with open('log0dot05_angle_ST_SC.csv','r') as csvfile:
#     plots = csv.reader(csvfile, delimiter=' ')
#     for row in plots:
#         # x.append(int(row[0]))
#         y.append((row[-1]))

# plt.plot(y, label='Loaded from file!')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Interesting Graph\nCheck it out')
# plt.legend()
# plt.show()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("pattern")
    args = parser.parse_args()
    print(args.pattern)

    pl = PlotCSV(args.pattern)
    pl.plotCSV()
