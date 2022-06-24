import sys
import subprocess
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPalette, QBrush, QPixmap
from PyQt5.QtWidgets import QDialog, QLabel, QPushButton


class guia(QDialog):
    def __init__(self):
        super(guia, self).__init__()
        self.initialize()

    def initialize(self):
        self.setWindowTitle("Guía para usar DICCI")
        self.setGeometry(555, 250, 381, 305)
        self.move(494, 232)
        self.setWindowFlags(Qt.FramelessWindowHint)
        wallpaper = QPalette()
        wallpaper.setBrush(self.backgroundRole(), QBrush(QPixmap("../Images/two.jpg")))
        self.setPalette(wallpaper)
        self.display_widgets()

    def display_widgets(self):
        self.lbl_Title = QLabel("¿Cómo usar DICCI?", self)
        self.lbl_Title.setGeometry(110, 27, 157, 30)
        self.lbl_Title.setFont(QFont("Univers", 12, QFont.Bold))
        self.lbl_Title.setStyleSheet("color: white;")

        self.lbl_1 = QLabel("Funciones:", self)
        self.lbl_1.setGeometry(29, 50, 200, 30)
        self.lbl_1.setFont(QFont("Univers", 9))
        self.lbl_1.setStyleSheet("color: white;")

        self.lbl_2 = QLabel("1.- Al presionar el botón 'Preguntar un significado a Dicci'\n"
                            "DICCI pedirá una palabra la cual desees saber su significado", self)
        self.lbl_2.setGeometry(29, 77, 500, 40)
        self.lbl_2.setFont(QFont("Univers", 9))
        self.lbl_2.setStyleSheet("color: white;")

        self.lbl_3 = QLabel("2.- Al activar el boton 'Reproducir video' DICCI pedirá que\n"
                            "digas por voz el nombre del video que quieras reproducir.", self)
        self.lbl_3.setGeometry(29, 112, 500, 40)
        self.lbl_3.setFont(QFont("Univers", 9))
        self.lbl_3.setStyleSheet("color: white;")

        self.lbl_4 = QLabel("3.- En caso DICCI no encuentre un significado a la palabra\n"
                            "que usteded requiera, puede utilizar el botón 'Alternativa\n"
                            "a palabra no encontrada' de esta manera se le redirigirá a\n"
                            "un sitio web de confianza el cual funciona como un \n"
                            "diccionario.", self)
        self.lbl_4.setGeometry(29, 155, 500, 40)
        self.lbl_4.setFont(QFont("Univers", 9))
        self.lbl_4.setStyleSheet("color: white;")

        self.lbl_5 = QLabel("Recomendación: Espere 2 segundos después de que DICCI\n"
                            "nos pregunte qué palabra deseamos buscar. De esta\n"
                            "manera DICCI podrá responder de forma efectiva.", self)
        self.lbl_5.setGeometry(29, 205, 500, 40)
        self.lbl_5.setFont(QFont("Univers", 9))
        self.lbl_5.setStyleSheet("color: white;")

        self.CloseFunct = QPushButton("X", self)
        self.CloseFunct.setFont(QFont("Univers", 9, QFont.Bold))
        self.CloseFunct.setGeometry(340, 20, 25, 20)
        self.CloseFunct.clicked.connect(self.closeBtn)
        self.CloseFunct.setStyleSheet("background-color: #37D9D5;"
                                      "color: black")

    def closeBtn(self):
        guia.close(self)





