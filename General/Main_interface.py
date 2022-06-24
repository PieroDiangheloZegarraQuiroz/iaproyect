import sys
import subprocess
import webbrowser

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QTextEdit, QLineEdit, QVBoxLayout, QFrame
from PyQt5.QtGui import QFont, QPixmap, QPalette, QBrush, QMovie
from PyQt5.QtCore import *
from time import strftime
from General import Functions
from General import Clock


class PrincipalWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.initUi()

    def initUi(self):
        self.setWindowTitle("Asistente Virtual Dicci")
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setFixedSize(735, 500)
        wallpaper = QPalette()
        wallpaper.setBrush(self.backgroundRole(), QBrush(QPixmap("../Images/Panel.jpg")))
        self.setPalette(wallpaper)

        self.display_widgets()

    def display_widgets(self):
        # Labels
        self.lblTitle1 = QLabel('ASISTENTE Virtual \n'
                                'Dicci', self)
        self.lblTitle1.setAlignment(Qt.AlignCenter)
        self.lblTitle1.setGeometry(16, 16, 255, 77)
        self.lblTitle1.setFont(QFont("ROG FONTS", 12, QFont.Bold))
        self.lblTitle1.setStyleSheet("border: 2px outset cyan;"
                                     "border-radius: 2px;"
                                     "color: white;")

        self.lblTitle2 = QLabel(self)
        self.lblTitle2.setPixmap(
            QPixmap("../Images/TittleImg.jpg").scaled(255, 103, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.lblTitle2.setGeometry(16, 16, 255, 77)
        self.lblTitle2.lower()

        self.lblDescriptionTittle = QLabel('Descripción', self)
        self.lblDescriptionTittle.setGeometry(53, 166, 140, 170)
        self.lblDescriptionTittle.setFont(QFont("Univers", 9, QFont.Bold))
        self.lblDescriptionTittle.setStyleSheet("color: white")

        self.lblDescription = QLabel('\n'
                                     '\n'
                                     'Hola, me llamo Dicci\n'
                                     'soy un asistente \n'
                                     'virtual y mi propósito \n'
                                     'es brindarte\n'
                                     'significados a las\n'
                                     'palabras que desees,\n'
                                     'así como también\n'
                                     'buscar videos que\n'
                                     'quieras reproducir.', self)
        self.lblDescription.setAlignment(Qt.AlignLeft)
        self.lblDescription.setGeometry(17, 235, 140, 170)
        self.lblDescription.setFont(QFont("Univers", 9, QFont.Bold))
        self.lblDescription.setStyleSheet("border: 2px outset #10a7f0;"
                                          "border-radius: 2px;"
                                          "color: white;"
                                          "background-color: #013950;")
        self.lblDescription.lower()

        # ===============================================================
        # Image #
        self.lblTitle2 = QLabel(self)
        self.lblTitle2.setPixmap(
            QPixmap("../Images/Books.jpg").scaled(190, 103, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.lblTitle2.setGeometry(470, 17, 100, 70)

        # Gif
        self.labelGif = QLabel(self)
        self.movie = QMovie('../Images/GifWave.gif')
        self.labelGif.setMovie(self.movie)
        self.labelGif.move(589, 13)
        self.labelGif.resize(140, 70)
        self.movie.start()

        # Image

        # self.Image = QLabel(self)
        # self.Image.setPixmap(QPixmap("../Images/Dicci_Logo.png").scaled(200, 220))
        # self.Image.setGeometry(200, 200, 300, 180)

        # Edit
        # self.Result = QTextEdit(self)
        # self.Result.setStyleSheet("border-radius: 10px;"
        #                           "background-color: rgba(201, 84, 84, 0.16);")
        # self.Result.setGeometry(120, 205, 380, 80)
        # self.Result.setFont(QFont("roboto", 8))

        # Buttons
        self.buttonFunction = QPushButton("¿Cómo usar Dicci?", self)
        self.buttonFunction.setFont(QFont("Univers", 8, QFont.Bold))
        self.buttonFunction.setGeometry(30, 124, 110, 80)
        self.buttonFunction.clicked.connect(self.most)
        self.buttonFunction.setStyleSheet("background-color: #013950;"
                                          "color: #98feff")

        self.buttonAlt = QPushButton("Alternativa a\n"
                                     "palabra no encontrada", self)
        self.buttonAlt.setFont(QFont("Universe", 9, QFont.Bold))
        self.buttonAlt.setGeometry(290, 17, 157, 50)
        self.buttonAlt.clicked.connect(self.open_webbrowser)
        self.buttonAlt.setStyleSheet("background-color: #013950;"
                                     "color: #98feff")

        self.buttonTalk = QPushButton("Preguntar un\nsignificado a\n"
                                      "Dicci", self)
        self.buttonTalk.setFont(QFont("Univers", 9, QFont.Bold))
        self.buttonTalk.setGeometry(600, 112, 100, 80)
        self.buttonTalk.clicked.connect(self.StartDicci)
        self.buttonTalk.setStyleSheet("background-color: #013950;"
                                      "color: #98feff")
        #
        self.buttonMusic = QPushButton("Reproducir video", self)
        self.buttonMusic.setFont(QFont("Univers", 8, QFont.Bold))
        self.buttonMusic.clicked.connect(self.StartRepMusic)
        self.buttonMusic.setGeometry(590, 247, 126, 30)
        self.buttonMusic.setStyleSheet("background-color: #013950;"
                                       "color: #98feff")
        # HORA DIGITAL
        self.buttonClose = QPushButton("Hora actual", self)
        self.buttonClose.setFont(QFont("Univers", 9, QFont.Bold))
        self.buttonClose.setGeometry(590, 349, 126, 30)
        self.buttonClose.clicked.connect(self.StartClock)
        self.buttonClose.setStyleSheet("background-color: #37D9D5;"
                                       "color: #black")

        self.buttonClock = QPushButton("Cerrar DICCI", self)
        self.buttonClock.setFont(QFont("Univers", 8, QFont.Bold))
        self.buttonClock.setGeometry(27, 443, 126, 23)
        self.buttonClock.clicked.connect(self.closeButton)
        self.buttonClock.setStyleSheet("background-color: #37D9D5;"
                                       "color: #black")

        self.FunctionsF = Functions.guia()
        self.ClockFrame = Clock.AppDemo()

    def open_webbrowser(self):
        webbrowser.open('https://www.wordreference.com/definicion/')

    def most(self):
        self.yn = True
        if self.yn:
            self.FunctionsF.show()
        self.yn = False

    def StartDicci(self):
        VoiceDicci = subprocess.run([sys.executable, '../General/VoiceDicci.py'])

    def StartRepMusic(self):
        RepMusic = subprocess.run([sys.executable, '../General/Rep_Music.py'])

    def StartClock(self):
        self.yn = True
        if self.yn:
            self.ClockFrame.show()
        self.yn = False

    #   Clock = subprocess.run([sys.executable, '../General/Clock.py'])

    def closeButton(self):
        sys.exit()


def main():
    app = QApplication(sys.argv)
    window = PrincipalWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
