# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainform.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(440, 602)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.exitBtn = QtWidgets.QPushButton(self.centralwidget)
        self.exitBtn.setGeometry(QtCore.QRect(10, 10, 89, 25))
        self.exitBtn.setObjectName("exitBtn")
        self.time = QtWidgets.QLabel(self.centralwidget)
        self.time.setGeometry(QtCore.QRect(210, 490, 211, 61))
        self.time.setWordWrap(False)
        self.time.setObjectName("time")
        self.connectString = QtWidgets.QLineEdit(self.centralwidget)
        self.connectString.setGeometry(QtCore.QRect(140, 10, 291, 25))
        self.connectString.setObjectName("connectString")
        self.user = QtWidgets.QLineEdit(self.centralwidget)
        self.user.setGeometry(QtCore.QRect(140, 40, 113, 25))
        self.user.setObjectName("user")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(310, 40, 121, 25))
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 40, 40, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(260, 40, 51, 17))
        self.label_2.setObjectName("label_2")
        self.connectBtn = QtWidgets.QPushButton(self.centralwidget)
        self.connectBtn.setGeometry(QtCore.QRect(10, 40, 89, 25))
        self.connectBtn.setObjectName("connectBtn")
        self.sql = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.sql.setEnabled(False)
        self.sql.setGeometry(QtCore.QRect(10, 90, 421, 111))
        self.sql.setPlaceholderText("")
        self.sql.setObjectName("sql")
        self.execSQL = QtWidgets.QPushButton(self.centralwidget)
        self.execSQL.setEnabled(False)
        self.execSQL.setGeometry(QtCore.QRect(20, 210, 89, 25))
        self.execSQL.setObjectName("execSQL")
        self.result = QtWidgets.QTableView(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(10, 240, 421, 251))
        self.result.setObjectName("result")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 440, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.exitBtn.clicked.connect(MainWindow.exit)
        self.connectBtn.clicked.connect(MainWindow.connect)
        self.execSQL.clicked.connect(MainWindow.execSQL1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.exitBtn.setText(_translate("MainWindow", "Exit"))
        self.time.setText(_translate("MainWindow", "TextLabel"))
        self.connectString.setText(_translate("MainWindow", "172.30.2.133:1521/test.home.ru"))
        self.user.setText(_translate("MainWindow", "u0"))
        self.password.setText(_translate("MainWindow", "u0"))
        self.label.setText(_translate("MainWindow", "User"))
        self.label_2.setText(_translate("MainWindow", "Passw"))
        self.connectBtn.setText(_translate("MainWindow", "Connect"))
        self.sql.setPlainText(_translate("MainWindow", "SELECT * FROM DUAL"))
        self.execSQL.setText(_translate("MainWindow", "Run"))

