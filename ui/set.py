# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\setting.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SettingForm(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    def setupUi(self, SettingForm):
        SettingForm.setObjectName("SettingForm")
        SettingForm.resize(400, 300)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        SettingForm.setFont(font)
        self.gridLayout = QtWidgets.QGridLayout(SettingForm)
        self.gridLayout.setObjectName("gridLayout")
        self.listView = QtWidgets.QListView(SettingForm)
        self.listView.setObjectName("listView")
        self.gridLayout.addWidget(self.listView, 0, 0, 4, 1)
        self.shooseFilePathButton = QtWidgets.QPushButton(SettingForm)
        self.shooseFilePathButton.setObjectName("shooseFilePathButton")
        self.gridLayout.addWidget(self.shooseFilePathButton, 0, 1, 1, 1)
        self.nowFilePathLabel = QtWidgets.QLabel(SettingForm)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.nowFilePathLabel.setFont(font)
        self.nowFilePathLabel.setObjectName("nowFilePathLabel")
        self.gridLayout.addWidget(self.nowFilePathLabel, 1, 1, 1, 1)
        self.addFilePathButton = QtWidgets.QPushButton(SettingForm)
        self.addFilePathButton.setObjectName("addFilePathButton")
        self.gridLayout.addWidget(self.addFilePathButton, 2, 1, 1, 1)
        self.delFilePathButton = QtWidgets.QPushButton(SettingForm)
        self.delFilePathButton.setObjectName("delFilePathButton")
        self.gridLayout.addWidget(self.delFilePathButton, 3, 1, 1, 1)
        self.syncAllFileButton = QtWidgets.QPushButton(SettingForm)
        self.syncAllFileButton.setObjectName("syncAllFileButton")
        self.gridLayout.addWidget(self.syncAllFileButton, 4, 0, 1, 1)
        self.openConfigButton = QtWidgets.QPushButton(SettingForm)
        self.openConfigButton.setObjectName("openConfigButton")
        self.gridLayout.addWidget(self.openConfigButton, 4, 1, 1, 1)

        self.retranslateUi(SettingForm)
        QtCore.QMetaObject.connectSlotsByName(SettingForm)

    def retranslateUi(self, SettingForm):
        _translate = QtCore.QCoreApplication.translate
        SettingForm.setWindowTitle(_translate("SettingForm", "设置"))
        self.shooseFilePathButton.setText(_translate("SettingForm", "选择"))
        self.nowFilePathLabel.setText(_translate("SettingForm", "当前选择："))
        self.addFilePathButton.setText(_translate("SettingForm", "加入"))
        self.delFilePathButton.setText(_translate("SettingForm", "删除"))
        self.syncAllFileButton.setText(_translate("SettingForm", "立刻全量同步"))
        self.openConfigButton.setText(_translate("SettingForm", "打开配置文件"))
