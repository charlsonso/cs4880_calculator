import time
import sys
from PyQt5.QtWidgets import (QApplication,
                             QWidget,
                             QPushButton,
                             QLabel)
from PyQt5.QtGui import * 
from PyQt5.QtCore import *


'''
how to figure out to display updated text?
when eval erors, send invalid text to text box
'''
class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Calculator'
        self.left = 10
        self.top  = 10
        self.width = 310
        self.height = 310

        self.equation=""
        self.display=""
        self.display_box = QLabel(self)
        self.display_box.move(10, 10)
        self.display_box.resize(100, 10)
        self.initUI()

    def update_display_box(self):
        if self.display == "":
            self.display_box.setText(self.equation)
        else:
            self.display_box.setText(self.display)


    def add_number_to_equation(self, value):
        self.equation = self.equation + value
        print(self.equation)
        self.update_display_box()

    def solve(self):
        self.display = str(eval(self.equation))
        print(self.display)
        self.equation = ""
        self.update_display_box()
        self.clear_equation()

    def clear_equation(self):
        self.equation=""
        self.display=""

    def clear_display(self):
        self.clear_equation()
        self.update_display_box()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,
                         self.top,
                         self.width,
                         self.height)
        
        calculator_button_title = ()

        # Generate 9 buttons
        # 
        # Add button titles '0-9'
#        for i in range(0,10):
#            calculator_button_title.append(str(i))
        # Add . C Symbols
#            calculator_button_title.append(('.', 'C')


        
        self.nine = QPushButton('9', self)
        self.nine.clicked.connect(lambda: self.add_number_to_equation(value = '9'))
        self.nine.resize(50, 50)
        self.nine.move(130, 70)

        self.eight = QPushButton('8', self)
        self.eight.clicked.connect(lambda: self.add_number_to_equation(value = '8'))
        self.eight.resize(50, 50)
        self.eight.move(70, 70)

        self.seven = QPushButton('7', self)
        self.seven.clicked.connect(lambda: self.add_number_to_equation(value = '7'))
        self.seven.resize(50, 50)
        self.seven.move(10, 70)
 
        self.six = QPushButton('6', self)
        self.six.clicked.connect(lambda: self.add_number_to_equation(value = '6'))
        self.six.resize(50, 50)
        self.six.move(130, 130)
 
        self.five = QPushButton('5', self)
        self.five.clicked.connect(lambda: self.add_number_to_equation(value = '5'))
        self.five.resize(50, 50)
        self.five.move(70, 130)
 
        self.four = QPushButton('4', self)
        self.four.clicked.connect(lambda: self.add_number_to_equation(value = '4'))
        self.four.resize(50, 50)
        self.four.move(10, 130)
 
        self.three = QPushButton('3', self)
        self.three.clicked.connect(lambda:self.add_number_to_equation(value='3'))
        self.three.resize(50, 50)
        self.three.move(130, 190)

        self.two = QPushButton('2', self)
        self.two.clicked.connect(lambda:self.add_number_to_equation(value='2'))
        self.two.resize(50, 50)
        self.two.move(70, 190)
 
        self.one = QPushButton('1', self)
        self.one.clicked.connect(lambda:self.add_number_to_equation(value='1'))
        self.one.resize(50, 50)
        self.one.move(10, 190)
 
        self.zero = QPushButton('0', self)
        self.zero.clicked.connect(lambda:self.add_number_to_equation(value='0'))
        self.zero.resize(50, 50)
        self.zero.move(10, 250)
 
        self.period = QPushButton('.', self)
        self.period.clicked.connect(lambda:self.add_number_to_equation(value='.'))
        self.period.resize(50, 50)
        self.period.move(70, 250)
 
        self.clear = QPushButton('C', self)
        self.clear.clicked.connect(self.clear_display)
        self.clear.resize(50, 50)
        self.clear.move(130, 250)

        self.plus = QPushButton('+', self)
        self.plus.clicked.connect(lambda: self.add_number_to_equation(value='+'))
        self.plus.resize(50, 50)
        self.plus.move(190, 70)

        self.minus = QPushButton('-', self)
        self.minus.clicked.connect(lambda: self.add_number_to_equation(value='-'))
        self.minus.resize(50, 50)
        self.minus.move(190, 130)

        self.times = QPushButton('*', self)
        self.times.clicked.connect(lambda: self.add_number_to_equation(value='*'))
        self.times.resize(50, 50)
        self.times.move(190, 190)

        self.division = QPushButton('/', self)
        self.division.clicked.connect(lambda: self.add_number_to_equation(value='-'))
        self.division.resize(50, 50)
        self.division.move(190, 250)
        
        self.equal = QPushButton('=', self)
        self.equal.clicked.connect(self.solve)
        self.equal.resize(50, 50)
        self.equal.move(250, 250)

        self.update_display_box()
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
