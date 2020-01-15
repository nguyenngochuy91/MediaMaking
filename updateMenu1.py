# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'updateMenu1.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5.QtWidgets import (QWidget, QSlider, QLineEdit, QLabel, QPushButton, QScrollArea,QApplication,
                             QHBoxLayout, QVBoxLayout, QMainWindow,QCheckBox)
from PyQt5.QtCore import Qt, QSize
from PyQt5 import QtWidgets,QtCore,QtGui
from bottle import Bottle

class Ui_updateMenu1(object):
    def setupUi(self, Form,home):
        self.home = home
        self.form = Form
        Form.setObjectName("updateMenu1")
        Form.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("microbiology.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Form)
        self.centralwidget.setObjectName("centralwidget")

        
        self.centralwidget = QtWidgets.QWidget(Form)
        # self.centralWidget.setObjectName("centralWidget")
        layout = QtWidgets.QVBoxLayout(self.centralwidget)
    
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        # self.scrollArea.setGeometry(QtCore.QRect(0, 0, 1131, 951))
        # self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        # self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        # self.scrollArea.setWidgetResizable(True)
        # self.scrollArea.setObjectName("scrollArea")
        # self.scrollArea.setEnabled(True)
        layout.addWidget(self.scrollArea)
    
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(300, 400, 500, 500))
        # self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
    
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
    
        layout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.label_2 = QtWidgets.QLabel("<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#ff55ff;\">Please check on the media to update</span></p><p align=\"center\"><br/></p></body></html>")
        self.label_2.setGeometry(QtCore.QRect(80, 0, 631, 51))
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        layout.addWidget(self.label_2)
        self.allCheckBox = []
        
        for i in range(1,50):
            object = QCheckBox("Checkbox {}".format(i))
            self.allCheckBox.append(object)
            layout.addWidget(object)            
            layout.addSpacing(20)
        
        # Ok button
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(320, 250, 61, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.ok)


        # Cancel button
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(500, 250, 61, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.goMainMenu)
        
        
        self.menubar = QtWidgets.QMenuBar(Form)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        Form.setMenuBar(self.menubar)
        
    
        self.statusbar = QtWidgets.QStatusBar(Form)
        self.statusbar.setObjectName("statusbar")
        Form.setStatusBar(self.statusbar)
        Form.setCentralWidget(self.centralwidget)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("updateMenu1", "MainWindow"))
#        self.label_2.setText(_translate("updateMenu1", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#ff55ff;\">Main Menu</span></p><p align=\"center\"><br/></p></body></html>"))
        self.pushButton.setText(_translate("Form", "OK"))
        self.pushButton_2.setText(_translate("Form", "Cancel"))
        
    # generate all the check label
    def generateLabels(self,layout):
        root = self.home.root
        return
        
## button executions
    # cancel button, go back to mainMenu
    def goMainMenu(self):
        self.home.showWindow("mainMenu")
    # ok button, store it into a bottle object, and go to menu
    def ok(self):
        # check if all the fields are valid
        self.vals = []
        for field,fieldName in self.fields:
            state = field.validator.validate(field.text(),0)[0]
            if state == QtGui.QValidator.Acceptable:
                self.vals.append(field.text())
            else:
                # prompt the user ofr the problem 
                QtWidgets.QMessageBox.information(self.home.window, 'Error', 'You have enter invalid data in field {}!'.format(fieldName), QtWidgets.QMessageBox.Ok)
                field.setFocusPolicy(QtCore.Qt.StrongFocus)
                field.setFocus()
                return 
        self.vals.append(self.plainTextEdit.toPlainText())
        # store info into our self.root bottle object
#        print (self.vals)
        self.home.root = Bottle(self.vals[0],self.vals[1],self.vals[2],self.vals[3],[],None)
        # go to next menu
        self.home.showWindow("mainMenu")
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QMainWindow()
    ui = Ui_updateMenu1()
    ui.setupUi(Form,None)
    Form.show()
    sys.exit(app.exec_())
