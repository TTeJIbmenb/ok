
from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QApplication,QHBoxLayout, QWidget, QRadioButton, QPushButton, QLabel, QVBoxLayout, QMessageBox
Bruh = QApplication([])

bro = QWidget()
bro.show()
bro.setWindowTitle("Конкурс от Crazy People")
bro.move(900,70)
bro.resize(400,200)
ghosy = QLabel("В каком году канал получил \"золотую кнопку\" от YouTube?")
a = QRadioButton("2005")
b = QRadioButton("2010")
c = QRadioButton("2015")
button= QRadioButton("2020")
g = QHBoxLayout()
gor = QHBoxLayout()
goriz = QHBoxLayout()
v = QVBoxLayout()
g.addWidget(ghosy)
gor.addWidget(a)
gor.addWidget(b)
goriz.addWidget(c)
goriz.addWidget(button)
v.addLayout(g)
v.addLayout(gor)
v.addLayout(goriz)
bro.setLayout(v)
bro.show()
def h():
    win = QMessageBox()
    win.setText("Верно! Вы выиграли гироскутер")
    win.exec_()
def i():
    win = QMessageBox()
    win.setText("Het,YOU Jl O X!!!")
    win.exec_()
c.clicked.connect(h)
a.clicked.connect(i)
b.clicked.connect(i)
button.clicked.connect(i)
Bruh.exec_()


