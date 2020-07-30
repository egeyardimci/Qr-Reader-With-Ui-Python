from PyQt5 import uic, QtWidgets , QtCore , QtGui
import sys
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLineEdit
import pyqrcodeng

class Ui(QtWidgets.QMainWindow,QPushButton,QLineEdit):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('qrReader.ui', self)
        self.pushButton_okut.clicked.connect(self.qrRead)
        self.pushButton_yaz.clicked.connect(self.qrWrite)

    def qrRead(self):
            import pyautogui ,os
            pyautogui.screenshot("qr.png")
            import cv2
            import numpy
            import pyzbar.pyzbar as pyzbar

            image = cv2.imread("qr.png")

            decodedObjects = pyzbar.decode(image)
            for obj in decodedObjects:
                data = str(obj.data)
            try:
                self.lineEdit_okut.setText(data[1:])
            except:
                self.lineEdit_okut.setText("Could not find a QR Code.")

    def qrWrite(self):
        value = self.lineEdit_yaz.text()
        self.pyqr(value)
        self.lineEdit_yaz.setText("Qr Code is ready in files!")

    def pyqr(self,value):
        q = pyqrcodeng.create(value)
        q.png("Qr_ready.png",scale=6)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    window.show()
    sys.exit(app.exec_())
