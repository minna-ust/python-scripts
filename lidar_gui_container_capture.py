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
        self.labelHangerCenterHeight = Label(self.root,text="吊具中心高度：").grid(row = 0,column =4)
        self.labelDistanceLidarBox = Label(self.root,text="箱侧面与雷达横向距离：").grid(row = 1,column =0)
        self.labelDistanceLidarHanger = Label(self.root,text="吊具与雷达横向距离：").grid(row = 1,column =2)
        self.labelHangerHeight = Label(self.root, text="吊具高度: ").grid(row=1, column = 4)
        self.labelBoxHeight = Label(self.root, text="集装箱高度: ").grid(row=1, column=6)
        self.labelAngleBox = Label(self.root,text="箱侧面与雷达形成的辐射角：").grid(row = 2,column =0)
        self.labelAngleHanger = Label(self.root,text="吊具与雷达形成的辐射角：").grid(row = 2,column =2)
        self.labelPointCountsBox = Label(self.root,text="箱侧面与雷达形成的点数：").grid(row = 3,column =0)
        self.labelPointCountsHanger = Label(self.root,text="吊具与雷达形成的点数：").grid(row = 3,column =2)
        # 创建一个输入框,并设置尺寸
        self.lidarHeightInput = Entry(self.root,width=10)
        self.boxCenterHeightInput = Entry(self.root, width=10)
        self.hangerCenterHeightInput = Entry(self.root, width=10)
        self.distanceLidarBoxInput = Entry(self.root, width=10)
        self.distanceLidarHangerInput = Entry(self.root, width=10)
        self.hangerHeightInput = Entry(self.root, width=10)
        self.hangerHeightInput.insert(10, "hanger height")
        self.boxHeightInput = Entry(self.root, width=10)
        self.boxHeightInput.insert(10, "box height")
        # 创建一个回显列表
        self.displayAngleBox = Listbox(self.root, width=12)
        self.displayAngleHanger = Listbox(self.root, width=12)
        self.displayPointCountsBox = Listbox(self.root, width=12)
        self.displayPointCountsHanger = Listbox(self.root, width=12)

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
        self.hangerCenterHeightInput.grid(row=0, column=5)
        self.distanceLidarBoxInput.grid(row =1 ,column =1)
        self.distanceLidarHangerInput.grid(row=1, column=3)
        self.hangerHeightInput.grid(row=1, column=5)
        self.boxHeightInput.grid(row=1, column=7)
        self.displayAngleBox.grid(row=2, column =1)
        self.displayAngleHanger.grid(row=2, column =3)
        self.displayPointCountsBox.grid(row=3, column=1)
        self.displayPointCountsHanger.grid(row=3, column=3)
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
        # self.hangerCenterHeight = float(self.hangerCenterHeightInput.get())
        self.hangerCenterHeight = self.boxCenterHeight + 215.0
        self.distanceLidarBox = float(self.distanceLidarBoxInput.get())
        # self.distanceLidarHanger = float(self.distanceLidarHangerInput.get())
        self.distanceLidarHanger = self.distanceLidarBox + 45.0

        self.boxHeight = float(self.boxHeightInput.get())
        self.hangerHeight = float(self.hangerHeightInput.get())

        try:
            self.angleBox = degrees(
                                        atan( (abs(self.lidarHeight - self.boxCenterHeight) + self.boxHeight / 2)
                                                                  / self.distanceLidarBox)
                                        - atan( (abs(self.lidarHeight - self.boxCenterHeight) - self.boxHeight / 2)
                                                                  / self.distanceLidarBox)
                                   )
            self.angleHanger = degrees(
                                        atan( (abs(self.lidarHeight - self.hangerCenterHeight) + self.hangerHeight / 2)
                                                                  / self.distanceLidarHanger)
                                        - atan( (abs(self.lidarHeight - self.hangerCenterHeight) - self.hangerHeight / 2)
                                                                  / self.distanceLidarHanger)
                                   )
            self.pointCountsBox = (self.angleBox / 0.068 - 10) * 8   # lidar : 10 Hz, assume 10 points is not usable each line (8 lines)
            self.pointCountsHanger = (self.angleHanger / 0.068 - 10) * 8   # lidar : 10 Hz，
        except:
            print("calculate error")


        #清空回显列表可见部分,类似clear命令
        self.displayAngleBox.insert(0,"")
        self.displayAngleHanger.insert(0, "")
        self.displayPointCountsBox.insert(0, "")
        self.displayPointCountsHanger.insert(0, "")

        # 为回显列表赋值
        self.displayAngleBox.insert(0,self.angleBox)
        self.displayAngleHanger.insert(0, self.angleHanger)
        self.displayPointCountsBox.insert(0, self.pointCountsBox)
        self.displayPointCountsHanger.insert(0, self.pointCountsHanger)
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
