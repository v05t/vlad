from PyQt5.QtWidgets import*

app = QApplication([])
okno = QWidget()

mline = QHBoxLayout()
okno.setLayout(mline)
line2 = QVBoxLayout()
mline.addLayout(line2)

vvod1 = QLineEdit()
vvod2 = QLineEdit()
line2.addWidget(vvod1)
line2.addWidget(vvod2)


line3 = QVBoxLayout()
mline.addLayout(line3)


plus = QPushButton('+')
line3.addWidget(plus)

minus = QPushButton('-')
line3.addWidget(minus)

multiply = QPushButton('*')
line3.addWidget(multiply)

divide = QPushButton(':')
line3.addWidget(divide)


result = QLabel('?')
mline.addWidget(result)
result.setStyleSheet('QLabel{font-size:50px}')

def pribav():
    try:
        a = int(vvod1.text())
        b = int(vvod2.text())
        res = a + b
        result.setText(str(res))
    except:
        okno2 = QMessageBox()
        okno2.setText('Только числа!')
        okno2.exec_()

plus.clicked.connect(pribav)

def subtract():
    try:
        a = int(vvod1.text())
        b = int(vvod2.text())
        res2 = a - b
        result.setText(str(res2))
    except:
        okno2 = QMessageBox()
        okno2.setText('Только числа!')
        okno2.exec_()
minus.clicked.connect(subtract)

def delet():
    try:
        a = int(vvod1.text())
        b = int(vvod2.text())
        res2 = a / b
        result.setText(str(res2))
    except:
        okno2 = QMessageBox()
        okno2.setText('Только числа!')
        okno2.exec_()
divide.clicked.connect(delet)

def ymnow():
    try:
        a = int(vvod1.text())
        b = int(vvod2.text())
        res2 = a * b
        result.setText(str(res2))
    except:
        okno2 = QMessageBox()
        okno2.setText('Только числа!')
        okno2.exec_()
multiply.clicked.connect(ymnow)

okno.show()
app.exec_()
