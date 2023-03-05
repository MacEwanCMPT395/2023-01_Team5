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
        self.setGeometry(0, 0, 1900, 825) # x,y,w,h
        self.setFixedSize(QSize(1900, 825)) # w,h
        self.setStyleSheet("background-color: white")

        ''' putting the pictures in place'''
        self.label = QLabel(self)
        self.pixmap = QPixmap("C:\\Users\\ayesh\\Documents\\University\\cmpt 395\\test\\2023-01_Team5-Schedule-System-\\macewan header.png")
        self.label.setPixmap(self.pixmap)
        self.label.resize(self.pixmap.width(), self.pixmap.height())

        self.label1 = QLabel(self)
        self.pixmap = QPixmap("C:\\Users\\ayesh\\Documents\\University\\cmpt 395\\test\\2023-01_Team5-Schedule-System-\\downpic.jpg")
        self.label1.setPixmap(self.pixmap)
        self.label1.resize(self.pixmap.width(), self.pixmap.height())
        self.label1.move(13,275)

        '''the title at the top'''
        self.SCLabel = QLabel("SCHOOL OF CONTINUING EDUCATION",self)
        self.SCLabel.move(410,0)
        self.SCLabel.resize(1475,150)
        self.SCLabel.setFont(QFont('Arial',39)) #902a39
        self.SCLabel.setStyleSheet("QLabel { color : #902a39; }")

        '''the room number combo box'''
        self.roomLabel = QLabel("Room Number:",self)
        self.roomLabel.move (20,180)
        self.roomLabel.resize(200,30)
        self.roomLabel.setFont(QFont('Arial',12))
        self.roomLabel.setStyleSheet("QLabel { color : #902a39; }; font-weight: bold")
        self.roomNumber = QComboBox(self)
        self.roomNumber.move(190,180)
        self.roomNumber.resize(190,35)

        '''making the export button'''
        self.submit = QPushButton("EXPORT", self)
        self.submit.setGeometry(200,230,175,25)
        self.submit.setStyleSheet("QPushButton {background-color: #902a39; color: white}")
        #self.submit.clicked.connect(self.clickExport)

        '''making the redo button'''
        self.submit = QPushButton("START OVER", self)
        self.submit.setGeometry(20,230,175,25)
        self.submit.setStyleSheet("QPushButton {background-color: #902a39; color: white}")
        #self.submit.clicked.connect(self.clickRedo)

        '''table stuff'''
        self.roomSchedule = QTableWidget(self)
        self.roomSchedule.move(400,150)
        self.roomSchedule.resize(1475,657)
        self.roomSchedule.setStyleSheet("border: 2px solid black; color: #902a39; font-weight: bold")
        #self.roomSchedule.setAlignment(QtCore.Qt.AlignCenter) 

        # Giving the count for the Row   
        self.roomSchedule.setRowCount(15)  
    
        # Giving the count for the Column  
        self.roomSchedule.setColumnCount(3)  
    
        #initializing the coloumns and rows
        self.roomSchedule.setItem(0, 0, QTableWidgetItem("Time"))  
        self.roomSchedule.setItem(1, 0, QTableWidgetItem("8:00 AM"))  
        self.roomSchedule.setItem(2, 0, QTableWidgetItem("9:00 AM"))  
        self.roomSchedule.setItem(3, 0, QTableWidgetItem("10:00 AM"))  
        self.roomSchedule.setItem(4, 0, QTableWidgetItem("11:00 AM"))  
        self.roomSchedule.setItem(5, 0, QTableWidgetItem("12:00 PM"))  
        self.roomSchedule.setItem(6, 0, QTableWidgetItem("1:00 PM"))  
        self.roomSchedule.setItem(7, 0, QTableWidgetItem("2:00 PM"))
        self.roomSchedule.setItem(8, 0, QTableWidgetItem("3:00 PM"))  
        self.roomSchedule.setItem(9, 0, QTableWidgetItem("4:00 PM"))  
        self.roomSchedule.setItem(10, 0, QTableWidgetItem("5:00 PM"))  
        self.roomSchedule.setItem(11, 0, QTableWidgetItem("6:00 PM"))  
        self.roomSchedule.setItem(12, 0, QTableWidgetItem("7:00 PM"))  
        self.roomSchedule.setItem(13, 0, QTableWidgetItem("8:00 PM"))  
        self.roomSchedule.setItem(14, 0, QTableWidgetItem("9:00 PM")) 

        self.roomSchedule.setItem(0, 1, QTableWidgetItem("Monday/Wednesday"))
        self.roomSchedule.setItem(1, 1, QTableWidgetItem())  
        self.roomSchedule.setItem(2, 1, QTableWidgetItem())  
        self.roomSchedule.setItem(3, 1, QTableWidgetItem())  
        self.roomSchedule.setItem(4, 1, QTableWidgetItem())  
        self.roomSchedule.setItem(5, 1, QTableWidgetItem())  
        self.roomSchedule.setItem(6, 1, QTableWidgetItem())  
        self.roomSchedule.setItem(7, 1, QTableWidgetItem())
        self.roomSchedule.setItem(8, 1, QTableWidgetItem())  
        self.roomSchedule.setItem(9, 1, QTableWidgetItem())  
        self.roomSchedule.setItem(10, 1, QTableWidgetItem())  
        self.roomSchedule.setItem(11, 1, QTableWidgetItem())  
        self.roomSchedule.setItem(12, 1, QTableWidgetItem())  
        self.roomSchedule.setItem(13, 1, QTableWidgetItem())  
        self.roomSchedule.setItem(14, 1, QTableWidgetItem())
        
        self.roomSchedule.setItem(0, 2, QTableWidgetItem("Tuesday/Thursday"))
        self.roomSchedule.setItem(1, 2, QTableWidgetItem())  
        self.roomSchedule.setItem(2, 2, QTableWidgetItem())  
        self.roomSchedule.setItem(3, 2, QTableWidgetItem())  
        self.roomSchedule.setItem(4, 2, QTableWidgetItem())  
        self.roomSchedule.setItem(5, 2, QTableWidgetItem())  
        self.roomSchedule.setItem(6, 2, QTableWidgetItem())  
        self.roomSchedule.setItem(7, 2, QTableWidgetItem())
        self.roomSchedule.setItem(8, 2, QTableWidgetItem())  
        self.roomSchedule.setItem(9, 2, QTableWidgetItem())  
        self.roomSchedule.setItem(10, 2, QTableWidgetItem())  
        self.roomSchedule.setItem(11, 2, QTableWidgetItem())  
        self.roomSchedule.setItem(12, 2, QTableWidgetItem())  
        self.roomSchedule.setItem(13, 2, QTableWidgetItem())  
        self.roomSchedule.setItem(14, 2, QTableWidgetItem())

        #making the coloumns,rows, tables look pretty
        self.roomSchedule.verticalHeader().hide()
        self.roomSchedule.horizontalHeader().hide()
        self.roomSchedule.setColumnWidth(0, 100)
        self.roomSchedule.setColumnWidth(1,670)
        self.roomSchedule.setColumnWidth(2,670)
        #self.roomSchedule.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignCenter)

        #setting box to a color
        self.roomSchedule.item(1, 1).setBackground(QColor(125,125,125))

        '''showing the initial screen'''
        self.show()


    

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = MainWindow()
    #start the event loop
    App.exec()
    print("hello")