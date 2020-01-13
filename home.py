# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainPage.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import sys
from newExperiment import Ui_NewExperiment
from mainMenu import Ui_MainMenu

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        ## add all the widget class that store new experiment page,etc so that we just call this on the callback
        self.root = None
        self.pages = {"newExperiment":Ui_NewExperiment(),"mainMenu":Ui_MainMenu()}
        self.window = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(927, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("microbiology.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 210, 461, 311))
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("NhiHuy.jpg"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        
        
        # start new experiment button
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 100, 231, 27))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda: self.show("newExperiment"))
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 10, 631, 51))
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        
        
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 927, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        # open file
        self.actionOpen_File = QtWidgets.QAction(MainWindow)
        self.actionOpen_File.setCheckable(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("openFile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen_File.setIcon(icon1)
        self.actionOpen_File.setObjectName("actionOpen_File")
        self.actionOpen_File.triggered.connect(self.openFile) 
        
        # save file as
        self.actionSave_File_As = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("saveFIle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_File_As.setIcon(icon2)
        self.actionSave_File_As.setObjectName("actionSave_File_As")
        self.actionSave_File_As.triggered.connect(self.saveFile)         
        
        # exit
        self.actionExit = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon3)
        self.actionExit.setObjectName("actionExit")
        self.actionExit.triggered.connect(self.closeFile)          
        
        
        # documentation
        self.actionDocumentation = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("document.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDocumentation.setIcon(icon4)
        self.actionDocumentation.setObjectName("actionDocumentation")
        
        # save 
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setCheckable(False)
        self.actionSave.setIcon(icon2)
        self.actionSave.setObjectName("actionSave")
        self.actionSave.triggered.connect(self.saveFile) 
        
        
        self.menuFile.addAction(self.actionOpen_File)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_File_As)
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionDocumentation)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "NhiMediaTracking"))
        self.pushButton_2.setText(_translate("MainWindow", "Start new Experiment"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#ff55ff;\">Welcome to the Media Tracking Program</span></p></body></html>"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen_File.setText(_translate("MainWindow", "Open File"))
        self.actionOpen_File.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave_File_As.setText(_translate("MainWindow", "Save File As"))
        self.actionSave_File_As.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionDocumentation.setText(_translate("MainWindow", "Documentation"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        
    def openFile(self):
        name,_ = QFileDialog.getOpenFileName(MainWindow, "Open File")
        if name:
            # we store the file and bring us to another frame
            file = open(name,"r")
            
    def saveFile(self):
        name, _ = QFileDialog.getSaveFileName(MainWindow, "Save File")
        # implement saving ...
        
    def closeFile(self):
        sys.exit(app.exec_())
        
    def show(self,name):
        self.ui = self.pages[name]
        self.form = QtWidgets.QWidget()
        self.ui.setupUi(self.form,self)
        # we hide our current window
        self.window.hide()
        # we show the start new experiment
        self.form.show()

        
if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
