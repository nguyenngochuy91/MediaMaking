# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newExperiment.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from bottle import Bottle

class Ui_NewExperiment(object):
    def setupUi(self, Form,parent):
        self.parent = parent
        self.window = Form
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
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(140, 110, 701, 31))
        self.textEdit.setObjectName("textEdit")
        
        # Ph field
        self.textEdit_2 = QtWidgets.QTextEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(140, 160, 701, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        
        # date field
        self.textEdit_3 = QtWidgets.QTextEdit(Form)
        self.textEdit_3.setGeometry(QtCore.QRect(140, 210, 701, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        
        # notes field
        self.textEdit_4 = QtWidgets.QTextEdit(Form)
        self.textEdit_4.setGeometry(QtCore.QRect(140, 260, 701, 191))
        self.textEdit_4.setObjectName("textEdit_4")
        
        
        # Ok button
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(320, 500, 61, 41))
        self.pushButton.setObjectName("pushButton")
        
        # Cancel button
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(500, 500, 61, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.cancel)
        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "New Experiment"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#ff55ff;\">Start New Experiment</span></p></body></html>"))
        self.label.setText(_translate("Form", "Name:"))
        self.label_3.setText(_translate("Form", "Ph:"))
        self.label_4.setText(_translate("Form", "Date:"))
        self.label_5.setText(_translate("Form", "Notes:"))
        self.pushButton.setText(_translate("Form", "OK"))
        self.pushButton_2.setText(_translate("Form", "Cancel"))

    def cancel(self):
        self.window.hide()
        self.parent.show()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_NewExperiment()
    ui.setupUi(Form,None)
    Form.show()
    sys.exit(app.exec_())
