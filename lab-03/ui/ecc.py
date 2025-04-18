# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\ui\ecc.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = "../platforms"

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(160, 340, 71, 16))
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 220, 61, 16))
        self.label_2.setObjectName("label_2")
        self.btn_verify = QtWidgets.QPushButton(self.centralwidget)
        self.btn_verify.setGeometry(QtCore.QRect(520, 400, 75, 23))
        self.btn_verify.setObjectName("btn_verify")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(330, 60, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.txt_sig = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_sig.setGeometry(QtCore.QRect(230, 320, 381, 71))
        self.txt_sig.setObjectName("txt_sig")
        self.txt_info = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_info.setGeometry(QtCore.QRect(230, 200, 381, 71))
        self.txt_info.setObjectName("txt_info")
        self.bth_sign = QtWidgets.QPushButton(self.centralwidget)
        self.bth_sign.setGeometry(QtCore.QRect(240, 400, 75, 23))
        self.bth_sign.setObjectName("bth_sign")
        self.bth_geneKey = QtWidgets.QPushButton(self.centralwidget)
        self.bth_geneKey.setGeometry(QtCore.QRect(510, 70, 75, 23))
        self.bth_geneKey.setObjectName("bth_geneKey")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "Signature"))
        self.label_2.setText(_translate("MainWindow", "Information:"))
        self.btn_verify.setText(_translate("MainWindow", "Verify"))
        self.label.setText(_translate("MainWindow", "ECC Cipher"))
        self.bth_sign.setText(_translate("MainWindow", "Sign"))
        self.bth_geneKey.setText(_translate("MainWindow", "GeneKey"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
