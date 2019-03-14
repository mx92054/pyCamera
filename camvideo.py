# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'camvideo.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CamVideo(object):
    def setupUi(self, CamVideo):
        CamVideo.setObjectName("CamVideo")
        CamVideo.resize(1212, 757)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        CamVideo.setFont(font)
        self.centralwidget = QtWidgets.QWidget(CamVideo)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labVideo = QtWidgets.QLabel(self.groupBox)
        self.labVideo.setObjectName("labVideo")
        self.horizontalLayout_2.addWidget(self.labVideo)
        self.horizontalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnStart = QtWidgets.QPushButton(self.groupBox_2)
        self.btnStart.setObjectName("btnStart")
        self.verticalLayout.addWidget(self.btnStart)
        self.btnStop = QtWidgets.QPushButton(self.groupBox_2)
        self.btnStop.setObjectName("btnStop")
        self.verticalLayout.addWidget(self.btnStop)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.btnClose = QtWidgets.QPushButton(self.groupBox_2)
        self.btnClose.setObjectName("btnClose")
        self.verticalLayout.addWidget(self.btnClose)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.horizontalLayout.setStretch(0, 8)
        self.horizontalLayout.setStretch(1, 1)
        CamVideo.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CamVideo)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1212, 25))
        self.menubar.setObjectName("menubar")
        CamVideo.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CamVideo)
        self.statusbar.setObjectName("statusbar")
        CamVideo.setStatusBar(self.statusbar)

        self.retranslateUi(CamVideo)
        QtCore.QMetaObject.connectSlotsByName(CamVideo)

    def retranslateUi(self, CamVideo):
        _translate = QtCore.QCoreApplication.translate
        CamVideo.setWindowTitle(_translate("CamVideo", "MainWindow"))
        self.groupBox.setTitle(_translate("CamVideo", "Video"))
        self.labVideo.setText(_translate("CamVideo", "Vido"))
        self.groupBox_2.setTitle(_translate("CamVideo", "Operation"))
        self.btnStart.setText(_translate("CamVideo", "Start"))
        self.btnStop.setText(_translate("CamVideo", "Stop"))
        self.btnClose.setText(_translate("CamVideo", "Close"))

