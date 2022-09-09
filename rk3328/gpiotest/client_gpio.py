#!/usr/bin/python3

import socket
import time
import sys
from PyQt5.QtWidgets import (QWidget, QMainWindow, QGridLayout, QPushButton, QApplication, QLineEdit)

HOST = '192.168.86.33'   # The remote host
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

        self.statusBar()

        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('gpio test')
        self.show()

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
