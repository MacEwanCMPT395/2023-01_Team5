import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import settingText
import pandas as pd

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        '''making the schedule builder window'''
        self.acceptDrops()
        self.setWindowTitle("Schedule Builder")
        self.setGeometry(0, 0, 1900, 950) # x,y,w,h
        self.setFixedSize(QSize(1900, 950)) # w,h
        self.setStyleSheet("background-color: white")

        '''table stuff'''
        self.roomSchedule = QLabel("Room Schedule Goes Here",self)
        self.roomSchedule.move(400,150)
        self.roomSchedule.resize(1475,770)
        self.roomSchedule.setStyleSheet("border: 1px solid black")
        self.roomSchedule.setAlignment(QtCore.Qt.AlignCenter)

        ''' putting the pictures in place'''
        self.label = QLabel(self)
        self.pixmap = QPixmap("C:\\Users\\ayesh\\Documents\\University\\cmpt 395\\test\\2023-01_Team5-Schedule-System-\\macewan header.png")
        self.label.setPixmap(self.pixmap)
        self.label.resize(self.pixmap.width(), self.pixmap.height())

        self.SCLabel = QLabel("SCHOOL OF CONTINUING EDUCATION",self)
        self.SCLabel.move(410,0)
        self.SCLabel.resize(1475,150)
        self.SCLabel.setFont(QFont('Arial',39)) #902a39
        self.SCLabel.setStyleSheet("QLabel { color : #902a39; }")

        self.roomNumber = QComboBox()
        
        '''showing the initial screen'''
        self.show()



if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = MainWindow()
    #start the event loop
    App.exec()
    print("hello")