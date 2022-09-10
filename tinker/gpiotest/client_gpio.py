#!/usr/bin/python3

import socket
import time
import sys
from PyQt5.QtWidgets import (QWidget, QMainWindow, QGridLayout, QLabel, QStatusBar, QSlider, QPushButton, QApplication, QLineEdit)
from PyQt5.QtCore import Qt

HOST = '192.168.86.30'   # The remote host
PORT = 50007              # The same port as used by the server

sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

class Client_gpio(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.widget = QWidget()
        self.setCentralWidget(self.widget)

        StartTestbtn = QPushButton("Start Test", self)
        StopTestbtn = QPushButton("Stop Test", self)
        LedOnbtn = QPushButton("Led On", self)
        LedOffbtn = QPushButton("Led Off", self)
        Lcdredbtn = QPushButton("Lcd Red", self)
        Lcdgreenbtn = QPushButton("Lcd Green", self)
        Lcdbluebtn = QPushButton("Lcd Blue", self)
        Lcdyellowbtn = QPushButton("Lcd Yellow", self)
        Lcdcyanbtn = QPushButton("Lcd Cyan", self)
        Lcdpurplebtn = QPushButton("Lcd Purple", self)
        Lcdwhitebtn = QPushButton("Lcd White", self)
        Lcdblackbtn = QPushButton("Lcd Black", self)
        self.qle = QLineEdit(self)
        Lcdsendtxtbtn = QPushButton("Lcd Sendtxt", self)
        Servoleftbtn = QPushButton("Servo Left", self)
        Servomiddlebtn = QPushButton("Servo Middle", self)
        Servorightbtn = QPushButton("Servo Right", self)
        Servostopbtn = QPushButton("Servo Stop", self)
        self.red   = QLabel('R')
        self.red.setStyleSheet("QLabel{color:rgba(225,0,0,255);}")
        self.green = QLabel('G')
        self.green.setStyleSheet("QLabel{color:rgba(0,255,0,255);}")
        self.blue  = QLabel('B')
        self.blue.setStyleSheet("QLabel{color:rgba(0,0,255,255);}")
        self.sldr = QSlider(Qt.Horizontal, self)
        self.sldr.setRange(0, 255)
        self.sldg = QSlider(Qt.Horizontal, self)
        self.sldg.setRange(0, 255)
        self.sldb = QSlider(Qt.Horizontal, self)
        self.sldb.setRange(0, 255)
        self.servo = QLabel("Servo")
        self.servo.setStyleSheet("QLabel{color:rgba(125,63,255,255);}")
        self.sld = QSlider(Qt.Horizontal, self)
        self.sld.setRange(50, 100)

        grid = QGridLayout(self.widget)
        grid.setSpacing(10)
        grid.addWidget(StartTestbtn, 0, 0)
        grid.addWidget(StopTestbtn, 0, 3)
        grid.addWidget(LedOnbtn, 1, 0)
        grid.addWidget(LedOffbtn, 1, 1)
        grid.addWidget(Lcdredbtn, 2, 0)
        grid.addWidget(Lcdgreenbtn, 2, 1)
        grid.addWidget(Lcdbluebtn, 2, 2)
        grid.addWidget(Lcdyellowbtn, 2, 3)
        grid.addWidget(Lcdcyanbtn, 3, 0)
        grid.addWidget(Lcdpurplebtn, 3, 1)
        grid.addWidget(Lcdwhitebtn, 3, 2)
        grid.addWidget(Lcdblackbtn, 3, 3)
        grid.addWidget(self.qle, 3, 0, 3, 2)
        grid.addWidget(Lcdsendtxtbtn, 4, 3)
        grid.addWidget(Servoleftbtn, 5, 0)
        grid.addWidget(Servomiddlebtn, 5, 1)
        grid.addWidget(Servorightbtn, 5, 2)
        grid.addWidget(Servostopbtn, 5, 3)
        grid.addWidget(self.sldr, 5, 0, 5, 3)
        grid.addWidget(self.sldg, 6, 0, 6, 3)
        grid.addWidget(self.sldb, 7, 0, 7, 3)
        grid.addWidget(self.red,   7, 3)
        grid.addWidget(self.green, 8, 3)
        grid.addWidget(self.blue,  10, 3)
        grid.addWidget(self.sld, 8, 0, 8, 3)
        grid.addWidget(self.servo, 11, 3)

        self.widget.setLayout(grid)

        StartTestbtn.clicked.connect(self.buttonClicked)
        StopTestbtn.clicked.connect(self.buttonClicked)
        LedOnbtn.clicked.connect(self.buttonClicked)
        LedOffbtn.clicked.connect(self.buttonClicked)
        Lcdredbtn.clicked.connect(self.buttonClicked)
        Lcdgreenbtn.clicked.connect(self.buttonClicked)
        Lcdbluebtn.clicked.connect(self.buttonClicked)
        Lcdyellowbtn.clicked.connect(self.buttonClicked)
        Lcdcyanbtn.clicked.connect(self.buttonClicked)
        Lcdpurplebtn.clicked.connect(self.buttonClicked)
        Lcdwhitebtn.clicked.connect(self.buttonClicked)
        Lcdblackbtn.clicked.connect(self.buttonClicked)
        self.qle.textChanged[str].connect(self.onChanged)
        Lcdsendtxtbtn.clicked.connect(self.buttonClicked)
        Servoleftbtn.clicked.connect(self.buttonClicked)
        Servomiddlebtn.clicked.connect(self.buttonClicked)
        Servorightbtn.clicked.connect(self.buttonClicked)
        Servostopbtn.clicked.connect(self.buttonClicked)
        self.sldr.valueChanged[int].connect(self.lcdchangeValue)
        self.sldg.valueChanged[int].connect(self.lcdchangeValue)
        self.sldb.valueChanged[int].connect(self.lcdchangeValue)
        self.sld.valueChanged[int].connect(self.servochangeValue)

        self.statusBar()

        self.setGeometry(300, 300, 500, 600)
        self.setWindowTitle('gpio test')
        self.show()

    def lcdchangeValue(self):

        valr = str(self.sldr.value())
        if len(valr) == 1:
            valr = '00' + valr
        elif len(valr) == 2:
            valr = '0' + valr
        valg = str(self.sldg.value())
        if len(valg) == 1:
            valg = '00' + valg
        elif len(valg) == 2:
            valg = '0' + valg
        valb = str(self.sldb.value())
        if len(valb) == 1:
            valb = '00' + valb
        elif len(valb) == 2:
            valb = '0' + valb
        val = valr + valg + valb
        sock.sendall(val.encode('utf-8'))
        data = sock.recv(1024)
        self.statusBar().showMessage(repr(data))

    def servochangeValue(self):

        str_val = str(self.sld.value() + 300)
        sock.sendall(str_val.encode('utf-8'))
        data = sock.recv(1024)
        self.statusBar().showMessage(repr(data))

    def onChanged(self, text):

        self.qle.setText(text)
        self.update()

    def buttonClicked(self):

        sender = self.sender()
        if sender.text() == "Start Test":
            sock.sendall(b"start")
            data = sock.recv(1024)
            self.statusBar().showMessage(repr(data))
        elif sender.text() == "Stop Test":
            sock.sendall(b"bye")
            data = sock.recv(1024)
            self.statusBar().showMessage(repr(data))
        elif sender.text() == "Led On":
            sock.sendall(b"led_on")
            data = sock.recv(1024)
            self.statusBar().showMessage(repr(data))
        elif sender.text() == "Led Off":
            sock.sendall(b"led_off")
            data = sock.recv(1024)
            self.statusBar().showMessage(repr(data))
        if sender.text() == "Lcd Red":
            sock.sendall(b"lcd_red")
            data = sock.recv(1024)
            self.statusBar().showMessage(repr(data))
        elif sender.text() == "Lcd Green":
            sock.sendall(b"lcd_green")
            data = sock.recv(1024)
            self.statusBar().showMessage(repr(data))
        elif sender.text() == "Lcd Blue":
            sock.sendall(b"lcd_blue")
            data = sock.recv(1024)
            self.statusBar().showMessage(repr(data))
        elif sender.text() == "Lcd Yellow":
            sock.sendall(b"lcd_yellow")
            data = sock.recv(1024)
            self.statusBar().showMessage(repr(data))
        elif sender.text() == "Lcd Cyan":
            sock.sendall(b"lcd_cyan")
            data = sock.recv(1024)
            self.statusBar().showMessage(repr(data))
        elif sender.text() == "Lcd Purple":
            sock.sendall(b"lcd_purple")
            data = sock.recv(1024)
            self.statusBar().showMessage(repr(data))
        elif sender.text() == "Lcd White":
            sock.sendall(b"lcd_white")
            data = sock.recv(1024)
            self.statusBar().showMessage(repr(data))
        elif sender.text() == "Lcd Black":
            sock.sendall(b"lcd_black")
            data = sock.recv(1024)
            self.statusBar().showMessage(repr(data))
        elif sender.text() == "Lcd Sendtxt":
            if self.qle.text():
                msg = self.qle.text()
                msg = "Hello" + msg
                sock.sendall(bytearray(msg.encode('utf-8')))
                data = sock.recv(1024)
                self.statusBar().showMessage(repr(data))
        elif sender.text() == "Servo Left":
            sock.sendall(b"servo_left")
            data = sock.recv(1024)
            self.statusBar().showMessage(repr(data))
        elif sender.text() == "Servo Middle":
            sock.sendall(b"servo_middle")
            data = sock.recv(1024)
            self.statusBar().showMessage(repr(data))
        elif sender.text() == "Servo Right":
            sock.sendall(b"servo_right")
            data = sock.recv(1024)
            self.statusBar().showMessage(repr(data))
        elif sender.text() == "Servo Stop":
            sock.sendall(b"servo_stop")
            data = sock.recv(1024)
            self.statusBar().showMessage(repr(data))


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Client_gpio()
    sys.exit(app.exec_())
