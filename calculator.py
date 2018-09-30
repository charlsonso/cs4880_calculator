import time
import sys
from PyQt5.QtWidgets import (QApplication,
                             QWidget,
                             QPushButton,
                             QLabel)
from PyQt5.QtGui import QIcon


# create buttons
# create display
# create stuff

def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x/y

'''
class calculate():
    self.first = ""
        type: string
    self.second
        type: string
    self.operator

    def press an operator
        save into self.operator
        clear out screen
    
    def input_number
        if self.first == "":
        elif self.second == "":
        else:
            clear second number
            input into second number

    def clear
    def input

'''
display_value = "hi"
class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Calculator'
        self.left = 10
        self.top  = 10
        self.width = 250 
        self.height = 310
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,
                         self.top,
                         self.width,
                         self.height)

        self.nine = QPushButton('9', self)
#        self.one.clicked.connect(print(1))
        self.nine.resize(50, 50)
        self.nine.move(130, 70)


        self.eight = QPushButton('8', self)
#        self.one.clicked.connect(print(1))
        self.eight.resize(50, 50)
        self.eight.move(70, 70)

        self.seven = QPushButton('7', self)
#        self.one.clicked.connect(print(1))
        self.seven.resize(50, 50)
        self.seven.move(10, 70)
 
        self.six = QPushButton('6', self)
#        self.one.clicked.connect(print(1))
        self.six.resize(50, 50)
        self.six.move(130, 130)
 
        self.five = QPushButton('5', self)
#        self.one.clicked.connect(print(1))
        self.five.resize(50, 50)
        self.five.move(70, 130)
 
        self.four = QPushButton('4', self)
#        self.one.clicked.connect(print(1))
        self.four.resize(50, 50)
        self.four.move(10, 130)
 
        self.three = QPushButton('3', self)
#        self.one.clicked.connect(print(1))
        self.three.resize(50, 50)
        self.three.move(130, 190)

        self.two = QPushButton('2', self)
#        self.one.clicked.connect(print(1))
        self.two.resize(50, 50)
        self.two.move(70, 190)
 
        self.one = QPushButton('1', self)
#        self.one.clicked.connect(print(1))
        self.one.resize(50, 50)
        self.one.move(10, 190)
 
        self.zero = QPushButton('0', self)
#        self.one.clicked.connect(print(1))
        self.zero.resize(50, 50)
        self.zero.move(10, 250)
 
        self.period = QPushButton('.', self)
#        self.one.clicked.connect(print(1))
        self.period.resize(50, 50)
        self.period.move(70, 250)
 
        self.clear = QPushButton('C', self)
#        self.one.clicked.connect(print(1))
        self.clear.resize(50, 50)
        self.clear.move(130, 250)

        self.plus = QPushButton('+', self)
#        self.one.clicked.connect(print(1))
        self.plus.resize(50, 50)
        self.plus.move(190, 70)

        self.minus = QPushButton('-', self)
#        self.one.clicked.connect(print(1))
        self.minus.resize(50, 50)
        self.minus.move(190, 130)

        self.times = QPushButton('*', self)
#        self.one.clicked.connect(print(1))
        self.times.resize(50, 50)
        self.times.move(190, 190)

        self.division = QPushButton('/', self)
#        self.one.clicked.connect(print(1))
        self.division.resize(50, 50)
        self.division.move(190, 250)
        
        self.create_display_box()
        self.show()

    def create_display_box(self):
        self.display_box = QLabel(self)
        self.display_box.setText(display_value)

def main():
    while(1):
        time.sleep(1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
