import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic


class photo(QtWidgets.QDialog):
    def __init__(self,parent=None):
        super(photo, self).__init__(parent)
        uic.loadUi('EmployeeUpdate.ui', self)
        self.btn.clicked.connect(self.attachImage)

    def attachImage(self):
        lay = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.addWidget(self.imageLabel)
        path = "temp"
        pixMap = QtGui.QPixmap(path)
        self.imageLabel.setPixmap(pixMap)
        self.imageScrollArea.setWidgetResizable(True)
        self.imageLabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = photo()
    #window.attachImage()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()