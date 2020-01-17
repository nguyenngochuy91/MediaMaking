# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'updateMenu1.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5.QtWidgets import (QWidget, QSlider, QLineEdit, QLabel, QPushButton, QScrollArea,QApplication,
                             QHBoxLayout, QVBoxLayout, QMainWindow,QCheckBox,QMessageBox)
from PyQt5.QtCore import Qt, QSize
from PyQt5 import QtWidgets,QtCore,QtGui
#from bottle import Bottle
from functools import partial

class Validator(QtGui.QIntValidator):
    def validate(self, value, pos):
        text = value.strip().title()
        try:
            val = int(text)
            if val<0 or val>10:
                return QtGui.QValidator.Invalid, text, pos
            else:
                return QtGui.QValidator.Acceptable, text, pos
        except:
            # means that it has at least one letter
            return QtGui.QValidator.Invalid, text, pos
        return super(Validator, self).validate(value, pos)
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
        allLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        layout1 = QtWidgets.QVBoxLayout()
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        layout1.addWidget(self.scrollArea)
        allLayout.addLayout(layout1)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(300, 400, 500, 500))
        # self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
    
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
    
        layout2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.label_2 = QtWidgets.QLabel("<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#ff55ff;\">Please check on the media to update</span></p><p align=\"center\"><br/></p></body></html>")
        self.label_2.setGeometry(QtCore.QRect(80, 0, 631, 51))
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        layout2.addWidget(self.label_2)
        
        #### handle the checkbox
        # this map a node name, to a check box
        self.allCheckBox = {}    
        # a map for node to name from root
        self.nodeToName,self.nameToNode = self.home.root.generateNames()
        # generate the labels base on root node, and store it into our allcheckbox
        self.generateLabels(layout2)
        
        
        layout3 = QtWidgets.QHBoxLayout()
        allLayout.addLayout(layout3)
        # Ok button
        self.pushButton = QtWidgets.QPushButton()
        self.pushButton.setGeometry(QtCore.QRect(320, 250, 61, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.ok)


        # Cancel button
        self.pushButton_2 = QtWidgets.QPushButton()
        self.pushButton_2.setGeometry(QtCore.QRect(500, 250, 61, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.goMainMenu)
        
        layout3.addWidget(self.pushButton)
        layout3.addWidget(self.pushButton_2)
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
        self.lineEdits = [QLineEdit() for i in range(len(self.nodeToName))]
        for i in range(len(self.nodeToName)):
            node,name = self.nodeToName[i]
            label = QLabel("Media {}".format(name))
            self.lineEdits[i].validator = QtGui.QIntValidator(0,10)
            self.lineEdits[i].textChanged.connect(partial(self.checkState,i))
            self.lineEdits[i].textChanged.emit(self.lineEdits[i].text())
            self.lineEdits[i].setText("0")
            horizontalLayout = QtWidgets.QHBoxLayout()
            horizontalLayout.addWidget(label)
            horizontalLayout.addWidget(self.lineEdits[i])
            self.allCheckBox[name] = self.lineEdits[i]
            layout.addLayout(horizontalLayout)            
            layout.addSpacing(20)        
        return
    # check the label
        ## validation method for user input with color
    def checkState(self,index):
        print ("my index:",index)
        validator = self.lineEdits[index].validator
        # print (sender.text())
        state = validator.validate(self.lineEdits[index].text(), 0)[0]
        if state == QtGui.QValidator.Acceptable:
            color = '#c4df9b' # green
        elif state == QtGui.QValidator.Intermediate:
            color = '#fff79a' # yellow
        else:
            color = '#f6989d' # red
        self.lineEdits[index].setStyleSheet('QLineEdit { background-color: %s }' % color)
## button executions
    # cancel button, go back to mainMenu
    def goMainMenu(self):
        self.home.showWindow({"name":"mainMenu"})
    # ok button, store it into a bottle object, and go to menu
    def ok(self):
        # get all the check box that was check
        checkedNode = []
        for node,nodeName in self.nodeToName:
            checkbox = self.allCheckBox[nodeName]
            if checkbox.isChecked():
                checkedNode.append([node,nodeName])
        # we generate a message to show the user
        if checkedNode:
            message = "You have chose the following media(s):\n {}. \nPlease press Ok to proceed, or Cancel to checkmark more media".format(", ".join([item[1] for item in checkedNode]))
        else:
            message = "You have not chosen anything, pressing Ok to go back to Main Menu, Cancel to checkmark more media"
        # we create a qmessage box
        buttonReply = QMessageBox.question(self.home.window, 'Warning!!!', message, QMessageBox.Ok | QMessageBox.Cancel, QMessageBox.Ok)
        if buttonReply == QMessageBox.Ok:
            if checkedNode:
                # we share our checkedNode with our root home
                self.home.updateNodes = [item[0] for item in checkedNode] 
                # we show the updateMenu2 window
                self.home.showWindow({"name":"updateMenu2"})
            else:
                self.home.showWindow({"name":"mainMenu"})
        else:
            pass 
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QMainWindow()
    ui = Ui_updateMenu1()
    ui.setupUi(Form,None)
    Form.show()
    sys.exit(app.exec_())
