# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\askDateDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_askSyncDateDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    def setupUi(self, askSyncDateDialog):
        askSyncDateDialog.setObjectName("askSyncDateDialog")
        askSyncDateDialog.resize(382, 192)
        askSyncDateDialog.setMinimumSize(QtCore.QSize(382, 192))
        askSyncDateDialog.setMaximumSize(QtCore.QSize(382, 192))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        askSyncDateDialog.setFont(font)
        self.buttonBox = QtWidgets.QDialogButtonBox(askSyncDateDialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 150, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(askSyncDateDialog)
        self.label.setGeometry(QtCore.QRect(40, 30, 231, 16))
        self.label.setObjectName("label")
        self.yearLabel = QtWidgets.QLabel(askSyncDateDialog)
        self.yearLabel.setGeometry(QtCore.QRect(110, 80, 21, 16))
        self.yearLabel.setObjectName("yearLabel")
        self.mouthLabel = QtWidgets.QLabel(askSyncDateDialog)
        self.mouthLabel.setGeometry(QtCore.QRect(172, 80, 21, 21))
        self.mouthLabel.setObjectName("mouthLabel")
        self.dayLabel = QtWidgets.QLabel(askSyncDateDialog)
        self.dayLabel.setGeometry(QtCore.QRect(230, 80, 21, 16))
        self.dayLabel.setObjectName("dayLabel")
        self.yearspinBox = QtWidgets.QSpinBox(askSyncDateDialog)
        self.yearspinBox.setGeometry(QtCore.QRect(50, 80, 61, 22))
        self.yearspinBox.setMinimum(2000)
        self.yearspinBox.setMaximum(2077)
        self.yearspinBox.setObjectName("yearspinBox")
        self.monthspinBox_2 = QtWidgets.QSpinBox(askSyncDateDialog)
        self.monthspinBox_2.setGeometry(QtCore.QRect(130, 80, 41, 22))
        self.monthspinBox_2.setMinimum(1)
        self.monthspinBox_2.setMaximum(12)
        self.monthspinBox_2.setObjectName("monthspinBox_2")
        self.dayspinBox_3 = QtWidgets.QSpinBox(askSyncDateDialog)
        self.dayspinBox_3.setGeometry(QtCore.QRect(190, 80, 41, 22))
        self.dayspinBox_3.setMinimum(1)
        self.dayspinBox_3.setMaximum(31)
        self.dayspinBox_3.setObjectName("dayspinBox_3")

        self.retranslateUi(askSyncDateDialog)
        self.buttonBox.accepted.connect(askSyncDateDialog.accept) # type: ignore
        self.buttonBox.rejected.connect(askSyncDateDialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(askSyncDateDialog)

    def retranslateUi(self, askSyncDateDialog):
        _translate = QtCore.QCoreApplication.translate
        askSyncDateDialog.setWindowTitle(_translate("askSyncDateDialog", "选择同步时间"))
        self.label.setText(_translate("askSyncDateDialog", "同步以下时间后的展台照片"))
        self.yearLabel.setText(_translate("askSyncDateDialog", "年"))
        self.mouthLabel.setText(_translate("askSyncDateDialog", "月"))
        self.dayLabel.setText(_translate("askSyncDateDialog", "日"))
