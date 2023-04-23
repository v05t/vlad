from PyQt5.QtWidgets import*

app = QApplication([])
okno = QWidget()

line1 = QVBoxLayout()
okno.setLayout(line1)

text1 = QLabel('Нажми на кнопку')
line1.addWidget(text1)
text1.setStyleSheet('QLabel{font-size:100px; color: red;}')

but1 = QPushButton('Кнопка')
line1.addWidget(but1)
but1.setStyleSheet('''QPushButton{font-size:50px; 
background: qlineargradient(x1:0 y1:0, x2:1 y2:0, stop:0 red, stop:1 blue);
 color: yellow
}''')
okno.setStyleSheet('''QWidget{background-image: url("Shrek1.jpg");
}''')

line2 = QVBoxLayout()
line1.addLayout(line2)

okno.show()
app.exec_()
