# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\zyj\OneDrive\職訓電腦_專題\Python_QT\qtAzToSrt\win.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(518, 451)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(390, 400, 104, 32))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(20, 430, 481, 30))
        self.lineEdit.setObjectName("lineEdit")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(20, 210, 361, 221))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(100, 10, 341, 31))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_Transcribe = QtWidgets.QPushButton(Form)
        self.pushButton_Transcribe.setGeometry(QtCore.QRect(390, 250, 104, 32))
        self.pushButton_Transcribe.setObjectName("pushButton_Transcribe")
        self.lineEdit_AzKey = QtWidgets.QLineEdit(Form)
        self.lineEdit_AzKey.setGeometry(QtCore.QRect(100, 50, 250, 22))
        self.lineEdit_AzKey.setObjectName("lineEdit_AzKey")
        self.lineEdit_AzRegion = QtWidgets.QLineEdit(Form)
        self.lineEdit_AzRegion.setGeometry(QtCore.QRect(100, 80, 150, 22))
        self.lineEdit_AzRegion.setObjectName("lineEdit_AzRegion")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 52, 58, 15))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 83, 58, 15))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(20, 115, 71, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(20, 157, 71, 16))
        self.label_5.setObjectName("label_5")
        self.lineEdit_FilePath = QtWidgets.QLineEdit(Form)
        self.lineEdit_FilePath.setGeometry(QtCore.QRect(100, 110, 400, 30))
        self.lineEdit_FilePath.setObjectName("lineEdit_FilePath")
        self.lineEdit_FileOutput = QtWidgets.QLineEdit(Form)
        self.lineEdit_FileOutput.setGeometry(QtCore.QRect(100, 150, 400, 30))
        self.lineEdit_FileOutput.setObjectName("lineEdit_FileOutput")
        self.pushButton_OpenFile = QtWidgets.QPushButton(Form)
        self.pushButton_OpenFile.setGeometry(QtCore.QRect(390, 210, 104, 32))
        self.pushButton_OpenFile.setObjectName("pushButton_OpenFile")
        self.pushButton_importKeyRegion = QtWidgets.QPushButton(Form)
        self.pushButton_importKeyRegion.setGeometry(QtCore.QRect(370, 50, 131, 32))
        self.pushButton_importKeyRegion.setObjectName("pushButton_importKeyRegion")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(20, 190, 80, 16))
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Azure wav to srt"))
        self.pushButton.setText(_translate("Form", "輸出 utf-8"))
        self.label.setText(_translate("Form", "Azure 音頻 wav 轉 srt 字幕工具 v2"))
        self.pushButton_Transcribe.setText(_translate("Form", "連線轉換"))
        self.lineEdit_AzKey.setText(_translate("Form", "please_input_key"))
        self.lineEdit_AzRegion.setText(_translate("Form", "please_input_Region"))
        self.label_2.setText(_translate("Form", "Key:"))
        self.label_3.setText(_translate("Form", "Region:"))
        self.label_4.setText(_translate("Form", "檔案路徑："))
        self.label_5.setText(_translate("Form", "輸出路徑："))
        self.pushButton_OpenFile.setText(_translate("Form", "開啓檔案"))
        self.pushButton_importKeyRegion.setText(_translate("Form", "匯入 Key / Region"))
        self.label_6.setText(_translate("Form", "轉換訊息："))