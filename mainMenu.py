# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainMenu.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog

class Ui_MainMenu(object):
    def setupUi(self, MainWindow,home):
        self.home = home
        self.window = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(926, 598)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 20, 631, 51))
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        
        # Home
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(330, 170, 231, 27))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.goHome)
        
        # Update
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(330, 310, 231, 27))
        self.pushButton_3.setObjectName("pushButton_3")
        
        
        # Visualize
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(330, 380, 231, 27))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.visualize)
        
        # Analyze
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(330, 100, 231, 27))
        self.pushButton_5.setObjectName("pushButton_5")
        
        # Modify button
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(330, 240, 231, 27))
        self.pushButton_6.setObjectName("pushButton_6")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 926, 20))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionDecumentation = QtWidgets.QAction(MainWindow)
        
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
        
        self.menuFile.addAction(self.actionOpen_File)
        self.menuFile.addAction(self.actionSave_File_As)
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionDecumentation)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#ff55ff;\">Main Menu</span></p><p align=\"center\"><br/></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "Home"))
        self.pushButton_6.setText(_translate("MainWindow", "Modify"))
        self.pushButton_3.setText(_translate("MainWindow", "Update"))
        self.pushButton_4.setText(_translate("MainWindow", "Visualize"))
        self.pushButton_5.setText(_translate("MainWindow", "Analyze"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionDecumentation.setText(_translate("MainWindow", "Documentation"))
        self.actionDecumentation.setToolTip(_translate("MainWindow", "Documentation"))
        self.actionOpen_File.setText(_translate("MainWindow", "Open File"))
        self.actionSave_File_As.setText(_translate("MainWindow", "Save File As"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))


    def openFile(self):
        name,_ = QFileDialog.getOpenFileName(self.window, "Open File")
        if name:
            # we store the file and bring us to another frame
            file = open(name,"r")
            
    def saveFile(self):
        name, _ = QFileDialog.getSaveFileName(self.window, "Save File")
        # implement saving ...
        
    def closeFile(self):
        sys.exit(app.exec_())
        
    def goHome(self):
        self.home.current.hide()
        self.home.current = self.home.window
        self.home.current.show()
        
    def visualize(self):
        self.home.root.visualize()
        # self.home.root.writeJSON("data")
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainMenu()
    ui.setupUi(MainWindow,None)
    MainWindow.show()
    sys.exit(app.exec_())

