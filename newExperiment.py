# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newExperiment.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtWidgets import QMessageBox
from bottle import Bottle
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
        
class Ui_NewExperiment(object):
    def setupUi(self, Form,home):
        self.home = home
        self.form = Form
        Form.setObjectName("Form")
        Form.resize(923, 601)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("microbiology.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(130, 20, 631, 51))
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 120, 69, 17))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(50, 170, 69, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(50, 220, 69, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(50, 330, 69, 17))
        self.label_5.setObjectName("label_5")
        
        
        # name field
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(130, 110, 691, 31))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        regex=QtCore.QRegExp("[0-9a-z-A-Z_]+")
        self.lineEdit.validator = QtGui.QRegExpValidator(regex)
        self.lineEdit.textChanged.connect(lambda: self.check_state(self.lineEdit))
        self.lineEdit.textChanged.emit(self.lineEdit.text())
        
        # Ph field
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 160, 691, 31))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.validator = Validator(self.lineEdit_2)
        self.lineEdit_2.textChanged.connect(lambda: self.check_state(self.lineEdit_2))
        self.lineEdit_2.textChanged.emit(self.lineEdit_2.text())
        
        # date field
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 210, 691, 31))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        regex=QtCore.QRegExp("^\d{4}[\-\/\s]?((((0[13578])|(1[02]))[\-\/\s]?(([0-2][0-9])|(3[01])))|(((0[469])|(11))[\-\/\s]?(([0-2][0-9])|(30)))|(02[\-\/\s]?[0-2][0-9]))$")
        self.lineEdit_3.validator = QtGui.QRegExpValidator(regex)
        self.lineEdit_3.textChanged.connect(lambda: self.check_state(self.lineEdit_3))
        self.lineEdit_3.textChanged.emit(self.lineEdit_3.text())
        
        # notes fieldnder
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setGeometry(QtCore.QRect(130, 290, 701, 191))
        self.plainTextEdit.setObjectName("plainTextEdit")
        # regex=QtCore.QRegExp("[^\n]+")
        # self.plainTextEdit.validator = QtGui.QRegExpValidator(regex)
        # self.plainTextEdit.textChanged.connect(lambda: self.check_state(self.plainTextEdit))
        # self.plainTextEdit.textChanged.emit(self.plainTextEdit.toPlainText())   
        
        # fields
        self.fields = [(self.lineEdit,"name"),(self.lineEdit_2,"ph"),(self.lineEdit_3,"date")]
        
        # Ok button
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(320, 500, 61, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.ok)
        
        # Cancel button
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(500, 500, 61, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.cancel)
        
        
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(20, 240, 91, 16))
        self.label_6.setObjectName("label_6")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "New Experiment"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#ff55ff;\">Start New Experiment</span></p></body></html>"))
        self.label.setText(_translate("Form", "Name:"))
        self.label_3.setText(_translate("Form", "pH:"))
        self.label_4.setText(_translate("Form", "Date:"))
        self.label_5.setText(_translate("Form", "Notes:"))
        self.label_6.setText(_translate("Form", "(yyyy-mm-dd)"))
        self.pushButton.setText(_translate("Form", "OK"))
        self.pushButton_2.setText(_translate("Form", "Cancel"))
        
    ## validation method for user input with color
    def check_state(self,sender):
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
    # cancel button, go back to home
    def cancel(self):
        self.home.showWindow({"name":"mainMenu"})
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
        self.home.showWindow({"name":"Menu"})
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_NewExperiment()
    ui.setupUi(Form,None)
    Form.show()
    sys.exit(app.exec_())
