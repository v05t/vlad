from PyQt5.QtWidgets import*

app = QApplication([])
okno = QWidget()

main = QHBoxLayout()
okno.setLayout(main)

line1 = QVBoxLayout()
line2 = QVBoxLayout()
main.addLayout(line1)
main.addLayout(line2)

b1 = QPushButton('Дальше')
tx1 = QLabel('Результат')
line1.addWidget(b1)
line2.addWidget(tx1)
tx1.hide()

def next1():
    tx1.show()
    b1.hide()
b1.clicked.connect(next1)

okno.show()
app.exec_()         
