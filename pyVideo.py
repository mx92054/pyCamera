# -*- coding: UTF-8
# created by chenming

import sys
import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QDockWidget, QListWidget
from PyQt5.QtGui import *
from camvideo import Ui_CamVideo


class mywindow(QtWidgets.QMainWindow, Ui_CamVideo):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)

        # setting main window geometry
        desktop_geometry = QtWidgets.QApplication.desktop()  # 获取屏幕大小
        main_window_width = desktop_geometry.width()  # 屏幕的宽
        main_window_height = desktop_geometry.height()  # 屏幕的高
        rect = self.geometry()  # 获取窗口界面大小
        window_width = rect.width()  # 窗口界面的宽
        window_height = rect.height()  # 窗口界面的高
        x = (main_window_width - window_width) // 2  # 计算窗口左上角点横坐标
        y = (main_window_height - window_height) // 2  # 计算窗口左上角点纵坐标
        self.setGeometry(x, y, window_width, window_height)  # 设置窗口界面在屏幕上的位置

        # 无边框以及背景透明一般不会在主窗口中用到，一般使用在子窗口中，例如在子窗口中显示gif提示载入信息等等
        # self.setWindowFlags(Qt.FramelessWindowHint)     # 无边框
        # self.setAttribute(Qt.WA_TranslucentBackground)  # 背景透明


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = mywindow()
    window.show()
    sys.exit(app.exec_())
