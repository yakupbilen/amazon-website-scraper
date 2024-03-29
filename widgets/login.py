# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Yakup Bilen\PycharmProjects\database\widgets\uies\login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sql_queries
from connection import cursor,connection
import widgets.reader_main
from objects.select_data import Select
from PyQt5.QtGui import QIntValidator
from widgets.writer_main import Ui_WriterMain
from widgets.admin_main import Ui_AdminMain
from widgets.access_admin_main import Ui_AccessAdminMain
from widgets.saler_main import Ui_SalerMain
from widgets.saler_manager_main import Ui_SalerManager

class Ui_Login(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_Login, self).__init__()
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)


class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(600, 800)
        LoginWindow.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setStyleSheet("font: 24pt \"Impact\";")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.lblInfo = QtWidgets.QLabel(self.centralwidget)
        self.lblInfo.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblInfo.setFont(font)
        self.lblInfo.setStyleSheet("color:rgb(207, 0, 3);\n"
"margin-top:20px;")
        self.lblInfo.setObjectName("lblInfo")
        self.horizontalLayout_3.addWidget(self.lblInfo)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.formWidget = QtWidgets.QWidget(self.centralwidget)
        self.formWidget.setMinimumSize(QtCore.QSize(400, 0))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.formWidget.setFont(font)
        self.formWidget.setStyleSheet("")
        self.formWidget.setObjectName("formWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formWidget)
        self.formLayout.setContentsMargins(5, 5, 5, 50)
        self.formLayout.setHorizontalSpacing(0)
        self.formLayout.setVerticalSpacing(7)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formWidget)
        self.label.setMinimumSize(QtCore.QSize(40, 0))
        self.label.setStyleSheet("font: 16pt \"Times New Roman\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-image: url(:/icons/Oxygen-Icons.org-Oxygen-Places-user-identity.ico);\n"
"background-color: rgb(200, 200, 200);\n"
"border-left:5px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineId = QtWidgets.QLineEdit(self.formWidget)
        self.lineId.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.lineId.setFont(font)
        self.lineId.setStyleSheet("padding-left:20px;\n"
"border:none;\n"
"background-color: rgb(200, 200, 200);\n"
"border-right:5px;")
        self.lineId.setObjectName("lineId")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineId)
        self.label_2 = QtWidgets.QLabel(self.formWidget)
        self.label_2.setMinimumSize(QtCore.QSize(40, 0))
        self.label_2.setStyleSheet("font: 16pt \"Times New Roman\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-image: url(:/icons/Icons8-Windows-8-Security-Password-2.ico);\n"
"background-color: rgb(200, 200, 200);\n"
"border-left:5px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.linePassword = QtWidgets.QLineEdit(self.formWidget)
        self.linePassword.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.linePassword.setFont(font)
        self.linePassword.setStyleSheet("padding-left:20px;\n"
"border:none;\n"
"background-color: rgb(200, 200, 200);\n"
"border-right:5px;")
        self.linePassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.linePassword.setObjectName("linePassword")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.linePassword)
        self.horizontalLayout_2.addWidget(self.formWidget)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.btnLogin = QtWidgets.QPushButton(self.centralwidget)
        self.btnLogin.setMinimumSize(QtCore.QSize(275, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btnLogin.setFont(font)
        self.btnLogin.setStyleSheet("border-radius:5px;\n"
"\n"
"border:2px solid gray;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons8-login-30.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnLogin.setIcon(icon)
        self.btnLogin.setObjectName("btnLogin")
        self.horizontalLayout.addWidget(self.btnLogin)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem7)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem8)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 3)
        self.verticalLayout.setStretch(2, 2)
        self.verticalLayout.setStretch(4, 3)
        self.verticalLayout.setStretch(5, 3)
        self.verticalLayout.setStretch(6, 3)
        self.verticalLayout.setStretch(7, 3)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        LoginWindow.setCentralWidget(self.centralwidget)

        self.lineId.setValidator(QIntValidator())
        self.linePassword.returnPressed.connect(self.login)
        self.lineId.returnPressed.connect(self.login)
        self.btnLogin.clicked.connect(self.login)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def login(self):
        self.lblInfo.setStyleSheet("color:rgb(255, 0, 0);margin-top:20px;")
        id = self.lineId.text()
        password = self.linePassword.text()
        if id:
            id = int(id)
            account = Select.select_account(id)
            employee = Select.select_employee(id)
            if account.password == password:
                self.lblInfo.setStyleSheet("color:rgb(85, 255, 0);margin-top:20px;")
                self.lblInfo.setText("Login successful")
                if employee == "":
                    cursor.execute(sql_queries.delete_account, (id,))
                    connection.commit()
                    msg = QMessageBox()
                    msg.setText("Account deleted..")
                    msg.setIcon(QMessageBox.Warning)
                    msg.setStyleSheet("color:red;")
                    msg.exec_()
                elif employee.job == "DataReader":
                    self.mainWindow = widgets.reader_main.Ui_ReaderMainWindow2(id)
                    self.mainWindow.show()
                    self.centralwidget.window().close()
                elif employee.job == "DataWriter":
                    self.mainWindow = Ui_WriterMain(id)
                    self.mainWindow.show()
                    self.centralwidget.window().close()
                elif employee.job == "Admin":
                    self.mainWindow = Ui_AdminMain(id)
                    self.mainWindow.show()
                    self.centralwidget.window().close()
                elif employee.job == "AccessAdmin":
                    self.mainWindow = Ui_AccessAdminMain(id)
                    self.mainWindow.show()
                    self.centralwidget.window().close()
                elif employee.job == "Saler":
                    self.mainWindow = Ui_SalerMain(id)
                    self.mainWindow.show()
                    self.centralwidget.window().close()
                elif employee.job == "SalerManager":
                    self.mainWindow = Ui_SalerManager(id)
                    self.mainWindow.show()
                    self.centralwidget.window().close()
                else:
                    cursor.execute(sql_queries.delete_employee,(id,))
                    connection.commit()
                    cursor.execute(sql_queries.delete_account,(id,))
                    connection.commit()
                    msg = QMessageBox()
                    msg.setText("Account and Employee deleted..")
                    msg.setIcon(QMessageBox.Warning)
                    msg.setStyleSheet("color:red;")
                    msg.exec_()
            else:
                self.lblInfo.setText("Wrong Username or Password!!")
        else:
            self.lblInfo.setText("Wrong Username or Password!!")



    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "MainWindow"))
        self.label_3.setText(_translate("LoginWindow", "<html><head/><body><p align=\"center\">USER</p><p align=\"center\">LOGİN</p></body></html>"))
        self.label_4.setText(_translate("LoginWindow", "<html><head/><body><p align=\"center\">Welcome to my project</p><p align=\"center\"><br/></p></body></html>"))
        self.lblInfo.setText(_translate("LoginWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.lineId.setPlaceholderText(_translate("LoginWindow", "Id"))
        self.linePassword.setPlaceholderText(_translate("LoginWindow", "Password"))
        self.btnLogin.setText(_translate("LoginWindow", "Login"))
import icons_rc
