# -*- coding: utf-8 -*-
from tkinter import *
import pygeoip
from math import *

class FindLocation(object):
    def __init__(self):
        self.angle = 0.0
        # 创建主窗口,用于容纳其它组件
        self.root = Tk()
        # 给主窗口设置标题内容
        self.root.title("lidar gui")

        self.labelLidarHeight = Label(self.root,text="雷达高度：").grid(row = 0,column =0)
        self.labelBoxCenterHeight = Label(self.root,text="集装箱中心高度：").grid(row = 0,column =2)
        self.labelTruckSideCenterHeight = Label(self.root,text="集卡侧板中心高度：").grid(row = 0,column =4)
        self.labelDistanceLidarBox = Label(self.root,text="箱侧面与雷达横向距离：").grid(row = 1,column =0)
        self.labelDistanceLidarTruckSide = Label(self.root,text="集卡侧板与雷达横向距离：").grid(row = 1,column =2)
        self.labelTruckSideHeight = Label(self.root, text="集卡侧板高度: ").grid(row=1, column = 4)
        self.labelBoxHeight = Label(self.root, text="集装箱高度: ").grid(row=1, column=6)
        self.labelAngleBox = Label(self.root,text="箱侧面与雷达形成的辐射角：").grid(row = 2,column =0)
        self.labelAngleTruckSide = Label(self.root,text="集卡侧板与雷达形成的辐射角：").grid(row = 2,column =2)
        self.labelPointCountsBox = Label(self.root,text="箱侧面与雷达形成的点数：").grid(row = 3,column =0)
        self.labelPointCountsTruckSide = Label(self.root,text="集卡侧板与雷达形成的点数：").grid(row = 3,column =2)
        # 创建一个输入框,并设置尺寸
        self.lidarHeightInput = Entry(self.root,width=10)
        self.boxCenterHeightInput = Entry(self.root, width=10)
        self.truckSideCenterHeightInput = Entry(self.root, width=10)
        self.distanceLidarBoxInput = Entry(self.root, width=10)
        self.distanceLidarTruckSideInput = Entry(self.root, width=10)
        self.truckSideHeightInput = Entry(self.root, width=10)
        # self.truckSideHeightInput.insert(10, "truck side height")
        self.boxHeightInput = Entry(self.root, width=10)
        # self.boxHeightInput.insert(10, "box height")
        # 创建一个回显列表
        self.displayAngleBox = Listbox(self.root, width=12)
        self.displayAngleTruckSide = Listbox(self.root, width=12)
        self.displayPointCountsBox = Listbox(self.root, width=12)
        self.displayPointCountsTruckSide = Listbox(self.root, width=12)

        # 创建一个查询结果的按钮
        # self.resultButton = Button(self.root, command = self.find_position, text = "查询")
        self.resultButton = Button(self.root, command = self.calculate, text = "查询")
        self.infoButton = Button(self.root, text = "集装箱高260cm(估计值)")
        self.infoButton2 = Button(self.root, text = "吊具高60cm(估计值)")
        self.infoButton3 = Button(self.root, text = "吊具中心与集装箱中心高度差215cm(估计值),由于当吊具在集装箱1m高处就要给角度，所以要加上100cm")
        self.infoButton4 = Button(self.root, text = "吊具中心与集装箱中心横向距离45cm（估计值）")
        self.infoButton5 = Button(self.root, text = "激光角分辨率0.034(5Hz), 0.034*2(10Hz)")

    # 完成布局
    def gui_arrang(self):
        # self.ip_input.pack()
        self.lidarHeightInput.grid(row =0 ,column =1)
        self.boxCenterHeightInput.grid(row =0, column=3)
        self.truckSideCenterHeightInput.grid(row=0, column=5)
        self.distanceLidarBoxInput.grid(row =1 ,column =1)
        self.distanceLidarTruckSideInput.grid(row=1, column=3)
        self.truckSideHeightInput.grid(row=1, column=5)
        self.boxHeightInput.grid(row=1, column=7)
        self.displayAngleBox.grid(row=2, column =1)
        self.displayAngleTruckSide.grid(row=2, column =3)
        self.displayPointCountsBox.grid(row=3, column=1)
        self.displayPointCountsTruckSide.grid(row=3, column=3)
        # self.display_info.pack()
        # self.result_button.pack()
        self.resultButton.grid(row=4, column =0)
        self.infoButton.grid(row=5, column = 0)
        self.infoButton2.grid(row=6, column = 0)
        self.infoButton3.grid(row=7, column = 0)
        self.infoButton4.grid(row=8, column = 0)
        self.infoButton5.grid(row=9, column = 0)

    def calculate(self):
        # 获取输入信息
        self.lidarHeight = float(self.lidarHeightInput.get())
        self.boxCenterHeight = float(self.boxCenterHeightInput.get())
        self.truckSideCenterHeight = float(self.truckSideCenterHeightInput.get())

        self.boxHeight = float(self.boxHeightInput.get())
        self.truckSideHeight = float(self.truckSideHeightInput.get())

        self.distanceLidarBox = float(self.distanceLidarBoxInput.get())
        self.distanceLidarTruckSide = float(self.distanceLidarTruckSideInput.get())
        # self.distanceLidarTruckSide = self.distanceLidarBox
        try:
            self.angleBox = degrees(
                                        atan( (abs(self.lidarHeight - self.boxCenterHeight) + self.boxHeight / 2)
                                                                  / self.distanceLidarBox)
                                        - atan( (abs(self.lidarHeight - self.boxCenterHeight) - self.boxHeight / 2)
                                                                  / self.distanceLidarBox)
                                   )
            self.angleTruckSide = degrees(
                                        atan( (abs(self.lidarHeight - self.truckSideCenterHeight) + self.truckSideHeight / 2)
                                                                  / self.distanceLidarTruckSide)
                                        - atan( (abs(self.lidarHeight - self.truckSideCenterHeight) - self.truckSideHeight / 2)
                                                                  / self.distanceLidarTruckSide)
                                   )
            self.pointCountsBox = (self.angleBox / 0.068 - 10) * 8   # lidar : 10 Hz, assume 10 points is not usable each line (8 lines)
            self.pointCountsTruckSide = (self.angleTruckSide / 0.068 - 10) * 8   # lidar : 10 Hz，
        except:
            print("calculate error")


        #清空回显列表可见部分,类似clear命令
        self.displayAngleBox.insert(0,"")
        self.displayAngleTruckSide.insert(0, "")
        self.displayPointCountsBox.insert(0, "")
        self.displayPointCountsTruckSide.insert(0, "")

        # 为回显列表赋值
        self.displayAngleBox.insert(0,self.angleBox)
        self.displayAngleTruckSide.insert(0, self.angleTruckSide)
        self.displayPointCountsBox.insert(0, self.pointCountsBox)
        self.displayPointCountsTruckSide.insert(0, self.pointCountsTruckSide)
        # 这里的返回值,没啥用,就是为了好看


def main():
    # 初始化对象
    FL = FindLocation()
    # 进行布局
    FL.gui_arrang()
    # 主程序执行
    mainloop()
    pass


if __name__ == "__main__":
    main()
