import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QDialog
from PyQt5.QtGui import QFont, QPalette, QBrush, QPixmap
from PyQt5.QtCore import QTimer, QTime, Qt

class AppDemo(QDialog):
    def __init__(self):
        super().__init__()
        self.resize(162, 20)
        self.move(883, 529)
        self.setWindowFlags(Qt.FramelessWindowHint)
        wallpaper = QPalette()
        wallpaper.setBrush(self.backgroundRole(), QBrush(QPixmap("../Images/imgclock.png")))
        self.setPalette(wallpaper)

        layout = QVBoxLayout()

        self.lbl = QLabel()
        self.lbl.setAlignment(Qt.AlignRight)
        self.lbl.move(100, 100)
        self.lbl.setFont(QFont('PyQt5 QLCDNumber', 19))
        self.lbl.setStyleSheet("color: cyan;")

        layout.addWidget(self.lbl)
        self.setLayout(layout)

        self.CloseClock = QPushButton("X", self)
        self.CloseClock.setFont(QFont("Univers", 9, QFont.Bold))
        self.CloseClock.setGeometry(15, 17, 25, 20)
        self.CloseClock.clicked.connect(self.closeBtn)
        self.CloseClock.setStyleSheet("background-color: #37D9D5;"
                                      "color: black")

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)

        self.showTime()

    def showTime(self):
        currentTime = QTime.currentTime()

        displayTxt = currentTime.toString('hh:mm:ss')
        print(displayTxt)

        self.lbl.setText(displayTxt)

    def closeBtn(self):
        AppDemo.close(self)


