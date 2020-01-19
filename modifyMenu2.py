# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 23:28:18 2020

@author: huyn
"""

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'updateMenu1.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5.QtWidgets import (QWidget, QSlider, QLineEdit, QLabel, QPushButton, QScrollArea,QApplication,
                             QHBoxLayout, QVBoxLayout, QMainWindow,QCheckBox,QMessageBox,QFormLayout,QGroupBox)
from PyQt5.QtCore import Qt, QSize
from PyQt5 import QtWidgets,QtCore,QtGui
#from bottle import Bottle
from functools import partial
alphabet = "ABCDEFGHIJK"
class Validator(QtGui.QDoubleValidator):
    def validate(self, value, pos):
        text = value.strip().title()
        try:
            val = float(text)
            if val<0 or val>14:
                return QtGui.QValidator.Invalid, text, pos
            else:
                return QtGui.QValidator.Acceptable, text, pos
        except:
            # means that it has at least one letter
            for num in "0123456789":
                if num in text:
                    return QtGui.QValidator.Invalid, text, pos
            if text =="":
                return QtGui.QValidator.Intermediate, text, pos 
            return QtGui.QValidator.Acceptable, text, pos
        return super(Validator, self).validate(value, pos)
class Ui_modifyMenu2(object):
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
        self.label_2 = QtWidgets.QLabel("<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#ff55ff;\">Please fill the info for the media</span></p><p align=\"center\"><br/></p></body></html>")
        self.label_2.setGeometry(QtCore.QRect(80, 0, 631, 51))
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        layout2.addWidget(self.label_2)
        
        #### generate label and field to fill out
        # this map a node name, to a check box
        self.dic = {}    
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


        # Back button
        self.pushButton_3 = QtWidgets.QPushButton()
        self.pushButton_3.setGeometry(QtCore.QRect(680, 250, 61, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(lambda: self.home.showWindow({"name":"updateMenu1"}))
        
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
        self.dic = {}
        checkedNodes  = self.home.modifyNodes # (pydot,name,child)
        for node in checkedNodes:
            nodeName = node.name
            ph = QtWidgets.QLineEdit()
            date = QtWidgets.QLineEdit()
            notes = QtWidgets.QPlainTextEdit()
            self.dic[nodeName]= [ph,date,notes]
        for node in checkedNodes:
            nodeName = node.name
            ph,date,notes = self.dic[nodeName]
            mediaLayout = QVBoxLayout()
            label = QLabel("<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#ff55ff;\">{}</span></p><p align=\"center\"><br/></p></body></html>".format(nodeName))
            label.setTextFormat(QtCore.Qt.RichText)            
            mediaLayout.addWidget(label)
            smallLayout = QVBoxLayout()
            
            # ph
            phLayout = QHBoxLayout()
            phLayout.addWidget(QLabel("pH:   "))
            ph.validator = Validator(ph)
            ph.setText("")
            ph.textChanged.connect(partial(self.checkState,ph))
            ph.textChanged.emit(ph.text())     
            phLayout.addWidget(ph)
            smallLayout.addLayout(phLayout)
            
            # date
            dateLayout = QHBoxLayout()
            dateLayout.addWidget(QLabel("Date: "))
            regex=QtCore.QRegExp("^\d{4}[\-\/\s]?((((0[13578])|(1[02]))[\-\/\s]?(([0-2][0-9])|(3[01])))|(((0[469])|(11))[\-\/\s]?(([0-2][0-9])|(30)))|(02[\-\/\s]?[0-2][0-9]))$")
            date.validator = QtGui.QRegExpValidator(regex)
            date.setText("")
            date.textChanged.connect(partial(self.checkState,date))
            date.textChanged.emit(date.text())  
            dateLayout.addWidget(date)
            smallLayout.addLayout(dateLayout)
            
            # notes
            notesLayout = QHBoxLayout()
            notesLayout.addWidget(QLabel("Notes: "))     
            notesLayout.addWidget(notes)
            smallLayout.addLayout(notesLayout)
            

            mediaLayout.addLayout(smallLayout)           
            mediaLayout.addSpacing(20)  
            layout.addLayout(mediaLayout)
            layout.addSpacing(40)
        return
    # check the label
        ## validation method for user input with color
    def checkState(self,sender):
#        print ("my index:",index)
        validator = sender.validator
        # print (sender.text())
        state = validator.validate(sender.text(), 0)[0]
        if state == QtGui.QValidator.Acceptable:
            color = '#c4df9b' # green
        elif state == QtGui.QValidator.Intermediate:
            color = '#fff79a' # yellow
        else:
            color = '#f6989d' # red
        sender.setStyleSheet('QLineEdit { background-color: %s }' % color)
## button executions
    # cancel button, go back to modifyMenu1
    def goMainMenu(self):
        self.home.showWindow({"name":"modifyMenu1"})
    # ok button, store it into a bottle object, and go to menu
    def ok(self):
        # get all the info from each media name
        nodeToNewInfo = {} # key: node name, value: list of bottle
        checkedNodes  = self.home.modifyNodes # list of node

        for node in checkedNodes:
            nodeName = node.name
            ph,date,notes = self.dic[nodeName]
            states = {ph:"pH",date:"date"}
            output = []
            for field in states:
                state = field.validator.validate(field.text(),0)[0]
                if state == QtGui.QValidator.Acceptable:
                    val = field.text()
                    output.append(val)
                else:
                    # prompt the user ofr the problem 
                    QtWidgets.QMessageBox.information(self.home.window, 'Error', 'You have enter invalid data in row Media {}!'.format(nodeName), QtWidgets.QMessageBox.Ok)
                    field.setFocusPolicy(QtCore.Qt.StrongFocus)
                    field.setFocus()  
                    return
            output.append(notes.toPlainText())
            nodeToNewInfo[node] = output
        # here means that all input are correct, we double check with user
        if checkedNodes:
            message = "You have chose the following media(s):\n {}. \nPlease press Ok to proceed, or Cancel to modify more media".format(", ".join([node.name for item in checkedNodes]))

        # we create a qmessage box
        buttonReply = QMessageBox.question(self.home.window, 'Warning!!!', message, QMessageBox.Ok | QMessageBox.Cancel, QMessageBox.Ok)
        if buttonReply == QMessageBox.Ok:
            # lots to do, first of deep copy our self.home.root
            deepCopy = self.home.root.deepCopy()
            # we will display the one we will modify
            nodeNames = {item.name:"pink" for item in checkedNodes}
            text = "You are modifying the pink nodes"
            # from the deep copy, we update all the children
            # print (parentNameToNodes)
            for node in nodeToNewInfo:
                ph,date,notes = nodeToNewInfo[node]
                node.ph = ph
                node.date = date
                node.notes = notes
            # now we check with user if this is what they want    
            self.home.visualize(nodeNames,text)
            # check with user
            reply =  QMessageBox.question(self.home.window, 'Warning', "Please check if the graph is corrected, you can press Ok to proceed to main menu, or Cancel to modify more media",  QMessageBox.Ok | QMessageBox.Cancel, QMessageBox.Ok)
            if reply == QMessageBox.Ok:
                # we show the mainMenu window
                self.home.showWindow({"name":"mainMenu"})
            else:
                # we reset our selfhome root
                # we save self.home.root to our deepCoy
                self.home.root = deepCopy
                pass
        else:
            self.home.root = deepCopy
            pass 
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QMainWindow()
    ui = Ui_modifyMenu2()
    ui.setupUi(Form,None)
    Form.show()
    sys.exit(app.exec_())
