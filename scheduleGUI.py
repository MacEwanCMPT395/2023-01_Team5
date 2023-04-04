import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import settingText as setText
#import data_structures as dataStruc
from data_structures import *
import webapp
from data_structures import *
from algorithm import *
from cohorts import *
from request_rooms import *
import random
import xlwt
import re

# Subclass QMainWindow to customize your application's main window
class MainWindow2(QMainWindow):
    def __init__(self, listofRooms, week_numbers, cohortList):
        super().__init__()

        self.listofRooms = listofRooms
        self.start_date = week_numbers
        self.cohortList = cohortList
        '''making the schedule builder window'''
        self.acceptDrops()
        self.setWindowTitle("Schedule Builder")
        self.setGeometry(0, 0, 1900, 835) # x,y,w,h
        self.setFixedSize(QSize(1900, 835)) # w,h
        self.setStyleSheet("background-color: white")

        ''' putting the pictures in place'''
        self.label = QLabel(self)
        self.pixmap = QPixmap("macewan header.png")
        self.label.setPixmap(self.pixmap)
        self.label.resize(390, self.pixmap.height())

        self.label1 = QLabel(self)
        self.pixmap = QPixmap("downpic.jpg")
        self.label1.setPixmap(self.pixmap)
        #self.label1.resize(355,427)
        self.label1.resize(self.pixmap.width(),self.pixmap.height())
        self.label1.move(20,380)

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
        listofRooms.insert(0, "")
        #print("roomlistshit", self.listofRooms)
        for room in self.listofRooms:
              #print(type(room))
              #print(room.get_capacity())
              self.roomNumber.addItems([room.__str__()])
        self.ctext = ""
        self.roomNumber.activated.connect(self.roomChosen)

        '''week combo box'''
        self.weekLabel = QLabel("Week Number:",self)
        self.weekLabel.move (20,260)
        self.weekLabel.resize(200,30)
        self.weekLabel.setFont(QFont('Arial',12))
        self.weekLabel.setStyleSheet("QLabel { color : #902a39; }; font-weight: bold")
        self.weekNumber = QComboBox(self)
        self.weekNumber.move(190,260)
        self.weekNumber.resize(190,35)
        self.weekNumber.addItems(week_numbers)
        self.wtext = ""
        self.weekNumber.activated.connect(self.weekChosen)

        '''the cohort combo box'''
        self.cohortLabel = QLabel("Cohort:",self)
        self.cohortLabel.move (20,220)
        self.cohortLabel.resize(200,30)
        self.cohortLabel.setFont(QFont('Arial',12))
        self.cohortLabel.setStyleSheet("QLabel { color : #902a39; }; font-weight: bold")
        self.cohort = QComboBox(self)
        self.cohort.move(190,220)
        self.cohort.resize(190,35)
        cohortList.insert(0, "")
        for c in self.cohortList:
              self.cohort.addItems([str(c)])
        self.cohortText = ""
        self.cohort.activated.connect(self.cohortChosen)

        '''making the export button'''
        self.export = QPushButton("EXPORT", self)
        self.export.setGeometry(200,310,175,25)
        self.export.setStyleSheet("QPushButton {background-color: #902a39; color: white}")
        self.export.clicked.connect(self.clickExport)

        '''making the redo button'''
        self.redo = QPushButton("START OVER", self)
        self.redo.setGeometry(20,345,175,25)
        self.redo.setStyleSheet("QPushButton {background-color: #902a39; color: white}")
        self.redo.clicked.connect(self.clickRedo)

        '''making the submit button'''
        self.submit = QPushButton("SUBMIT", self)
        self.submit.setGeometry(20,310,175,25)
        self.submit.setStyleSheet("QPushButton {background-color: #902a39; color: white}")
        self.submit.clicked.connect(self.clickSubmit)

        '''making quit button'''
        self.quit = QPushButton("Quit", self)
        self.quit.setGeometry(200,345,175,25)
        self.quit.setStyleSheet("QPushButton {background-color: #902a39; color: white}")
        self.quit.clicked.connect(self.clickQuit)

        '''table stuff'''
        self.roomSchedule = QTableWidget(self)
        self.roomSchedule.move(400,150)
        self.roomSchedule.resize(1475,657)
        self.roomSchedule.setStyleSheet("border: 2px solid black; font-weight: bold")
        #self.roomSchedule.setAlignment(QtCore.Qt.AlignCenter)

        # Giving the count for the Row
        self.roomSchedule.setRowCount(26)

        # Giving the count for the Column
        self.roomSchedule.setColumnCount(5)

        #initializing the coloumns and rows
        self.roomSchedule.clearContents()
        self.roomSchedule.setItem(0, 0, QTableWidgetItem("Time"))
        self.roomSchedule.setItem(1, 0, QTableWidgetItem("8:00 AM"))
        self.roomSchedule.setItem(2, 0, QTableWidgetItem("8:30 AM"))
        self.roomSchedule.setItem(3, 0, QTableWidgetItem("9:00 AM"))
        self.roomSchedule.setItem(4, 0, QTableWidgetItem("9:30 AM"))
        self.roomSchedule.setItem(5, 0, QTableWidgetItem("10:30 AM"))
        self.roomSchedule.setItem(6, 0, QTableWidgetItem("11:00 AM"))
        self.roomSchedule.setItem(7, 0, QTableWidgetItem("11:30 AM"))
        self.roomSchedule.setItem(8, 0, QTableWidgetItem("12:00 PM"))
        self.roomSchedule.setItem(9, 0, QTableWidgetItem("12:30 PM"))
        self.roomSchedule.setItem(10, 0, QTableWidgetItem("1:00 PM"))
        self.roomSchedule.setItem(11, 0, QTableWidgetItem("1:30 PM"))
        self.roomSchedule.setItem(12, 0, QTableWidgetItem("2:00 PM"))
        self.roomSchedule.setItem(13, 0, QTableWidgetItem("2:30 PM"))
        self.roomSchedule.setItem(14, 0, QTableWidgetItem("3:00 PM"))
        self.roomSchedule.setItem(15, 0, QTableWidgetItem("3:30 PM"))
        self.roomSchedule.setItem(16, 0, QTableWidgetItem("4:00 PM"))
        self.roomSchedule.setItem(17, 0, QTableWidgetItem("4:30 PM"))
        self.roomSchedule.setItem(18, 0, QTableWidgetItem("5:00 PM"))
        self.roomSchedule.setItem(19, 0, QTableWidgetItem("5:30 PM"))
        self.roomSchedule.setItem(20, 0, QTableWidgetItem("6:00 PM"))
        self.roomSchedule.setItem(21, 0, QTableWidgetItem("6:30 PM"))
        self.roomSchedule.setItem(22, 0, QTableWidgetItem("7:00 PM"))
        self.roomSchedule.setItem(23, 0, QTableWidgetItem("7:30 PM"))
        self.roomSchedule.setItem(24, 0, QTableWidgetItem("8:00 PM"))
        self.roomSchedule.setItem(25, 0, QTableWidgetItem("8:30 PM"))

        self.roomSchedule.setItem(0, 1, QTableWidgetItem("Monday"))
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
        self.roomSchedule.setItem(15, 1, QTableWidgetItem())
        self.roomSchedule.setItem(16, 1, QTableWidgetItem())
        self.roomSchedule.setItem(17, 1, QTableWidgetItem())
        self.roomSchedule.setItem(18, 1, QTableWidgetItem())
        self.roomSchedule.setItem(19, 1, QTableWidgetItem())
        self.roomSchedule.setItem(20, 1, QTableWidgetItem())
        self.roomSchedule.setItem(21, 1, QTableWidgetItem())
        self.roomSchedule.setItem(22, 1, QTableWidgetItem())
        self.roomSchedule.setItem(23, 1, QTableWidgetItem())
        self.roomSchedule.setItem(24, 1, QTableWidgetItem())
        self.roomSchedule.setItem(25, 1, QTableWidgetItem())

        self.roomSchedule.setItem(0, 2, QTableWidgetItem("Tuesday"))
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
        self.roomSchedule.setItem(15, 2, QTableWidgetItem())
        self.roomSchedule.setItem(16, 2, QTableWidgetItem())
        self.roomSchedule.setItem(17, 2, QTableWidgetItem())
        self.roomSchedule.setItem(18, 2, QTableWidgetItem())
        self.roomSchedule.setItem(19, 2, QTableWidgetItem())
        self.roomSchedule.setItem(20, 2, QTableWidgetItem())
        self.roomSchedule.setItem(21, 2, QTableWidgetItem())
        self.roomSchedule.setItem(22, 2, QTableWidgetItem())
        self.roomSchedule.setItem(23, 2, QTableWidgetItem())
        self.roomSchedule.setItem(24, 2, QTableWidgetItem())
        self.roomSchedule.setItem(25, 2, QTableWidgetItem())

        self.roomSchedule.setItem(0, 3, QTableWidgetItem("Wednesday"))
        self.roomSchedule.setItem(1, 3, QTableWidgetItem())
        self.roomSchedule.setItem(2, 3, QTableWidgetItem())
        self.roomSchedule.setItem(3, 3, QTableWidgetItem())
        self.roomSchedule.setItem(4, 3, QTableWidgetItem())
        self.roomSchedule.setItem(5, 3, QTableWidgetItem())
        self.roomSchedule.setItem(6, 3, QTableWidgetItem())
        self.roomSchedule.setItem(7, 3, QTableWidgetItem())
        self.roomSchedule.setItem(8, 3, QTableWidgetItem())
        self.roomSchedule.setItem(9, 3, QTableWidgetItem())
        self.roomSchedule.setItem(10,3, QTableWidgetItem())
        self.roomSchedule.setItem(11, 3, QTableWidgetItem())
        self.roomSchedule.setItem(12, 3, QTableWidgetItem())
        self.roomSchedule.setItem(13, 3, QTableWidgetItem())
        self.roomSchedule.setItem(14, 3, QTableWidgetItem())
        self.roomSchedule.setItem(15, 3, QTableWidgetItem())
        self.roomSchedule.setItem(16, 3, QTableWidgetItem())
        self.roomSchedule.setItem(17, 3, QTableWidgetItem())
        self.roomSchedule.setItem(18, 3, QTableWidgetItem())
        self.roomSchedule.setItem(19, 3, QTableWidgetItem())
        self.roomSchedule.setItem(20, 3, QTableWidgetItem())
        self.roomSchedule.setItem(21, 3, QTableWidgetItem())
        self.roomSchedule.setItem(22, 3, QTableWidgetItem())
        self.roomSchedule.setItem(23, 3, QTableWidgetItem())
        self.roomSchedule.setItem(24, 3, QTableWidgetItem())
        self.roomSchedule.setItem(25, 3, QTableWidgetItem())

        self.roomSchedule.setItem(0, 4, QTableWidgetItem("Thursday"))
        self.roomSchedule.setItem(1, 4, QTableWidgetItem())
        self.roomSchedule.setItem(2, 4, QTableWidgetItem())
        self.roomSchedule.setItem(3, 4, QTableWidgetItem())
        self.roomSchedule.setItem(4, 4, QTableWidgetItem())
        self.roomSchedule.setItem(5, 4, QTableWidgetItem())
        self.roomSchedule.setItem(6, 4, QTableWidgetItem())
        self.roomSchedule.setItem(7, 4, QTableWidgetItem())
        self.roomSchedule.setItem(8, 4, QTableWidgetItem())
        self.roomSchedule.setItem(9, 4, QTableWidgetItem())
        self.roomSchedule.setItem(10,4, QTableWidgetItem())
        self.roomSchedule.setItem(11, 4, QTableWidgetItem())
        self.roomSchedule.setItem(12, 4, QTableWidgetItem())
        self.roomSchedule.setItem(13, 4, QTableWidgetItem())
        self.roomSchedule.setItem(14, 4, QTableWidgetItem())
        self.roomSchedule.setItem(15, 4, QTableWidgetItem())
        self.roomSchedule.setItem(16, 4, QTableWidgetItem())
        self.roomSchedule.setItem(17, 4, QTableWidgetItem())
        self.roomSchedule.setItem(18, 4, QTableWidgetItem())
        self.roomSchedule.setItem(19, 4, QTableWidgetItem())
        self.roomSchedule.setItem(20, 4, QTableWidgetItem())
        self.roomSchedule.setItem(21, 4, QTableWidgetItem())
        self.roomSchedule.setItem(22, 4, QTableWidgetItem())
        self.roomSchedule.setItem(23, 4, QTableWidgetItem())
        self.roomSchedule.setItem(24, 4, QTableWidgetItem())
        self.roomSchedule.setItem(25, 4, QTableWidgetItem())

        #making the coloumns,rows, tables look pretty
        self.roomSchedule.verticalHeader().hide()
        self.roomSchedule.horizontalHeader().hide()
        self.roomSchedule.setColumnWidth(0, 120)
        self.roomSchedule.setColumnWidth(1,330)
        self.roomSchedule.setColumnWidth(2,330)
        self.roomSchedule.setColumnWidth(3,330)
        self.roomSchedule.setColumnWidth(4,330)

        '''showing the initial screen'''
        #print(listofRooms)
        self.show()

    def clickQuit(self):
            self.close()
            #QtCore.QCoreApplication.quit()

    def clickExport(self):
                filename = QFileDialog.getSaveFileName(self, 'Save File', '', ".xls(*.xls)")
                wbk = xlwt.Workbook()
                if self.ctext != "":
                        sheet = wbk.add_sheet(str(self.ctext) + "_" + str(self.wtext), cell_overwrite_ok=True)
                elif self.cohortText != "":
                        sheet = wbk.add_sheet(str(self.cohortText) + "_" + str(self.wtext), cell_overwrite_ok=True)
                for currentColumn in range(self.roomSchedule.columnCount()):
                        for currentRow in range(self.roomSchedule.rowCount()):
                                text = str(self.roomSchedule.item(currentRow, currentColumn).text())
                                sheet.write(currentRow, currentColumn, text)
                wbk.save(filename[0])

    def roomChosen(self,index):
        self.ctext = self.roomNumber.itemText(index)  # Get the text at index.
        self.roomIndex = self.roomNumber.currentIndex()

    def weekChosen(self,index):
        self.wtext = self.weekNumber.itemText(index)  # Get the text at index.
        self.weekIndex = self.weekNumber.currentIndex()

    def cohortChosen(self,index):
        self.cohortText = self.cohort.itemText(index)
        self.cohortIndex = self.cohort.currentIndex()

    def clickRedo(self):
        self.close()
        setText.restart()

    def clickSubmit(self):
        #ctext = self.roomNumber.itemText(index)  # Get the text at index.
        #print("Current itemText", ctext)

        #print("Current room selected", self.ctext)
        #print("Current week selected", self.wtext)

        #print("room list", ROOMS)
        if self.cohortText != "":
                #print("week index: ", self.weekIndex)
                self.roomSchedule.clearContents()
                self.roomSchedule.setItem(0, 0, QTableWidgetItem("Time"))
                self.roomSchedule.setItem(1, 0, QTableWidgetItem("8:00 AM"))
                self.roomSchedule.setItem(2, 0, QTableWidgetItem("8:30 AM"))
                self.roomSchedule.setItem(3, 0, QTableWidgetItem("9:00 AM"))
                self.roomSchedule.setItem(4, 0, QTableWidgetItem("9:30 AM"))
                self.roomSchedule.setItem(5, 0, QTableWidgetItem("10:30 AM"))
                self.roomSchedule.setItem(6, 0, QTableWidgetItem("11:00 AM"))
                self.roomSchedule.setItem(7, 0, QTableWidgetItem("11:30 AM"))
                self.roomSchedule.setItem(8, 0, QTableWidgetItem("12:00 PM"))
                self.roomSchedule.setItem(9, 0, QTableWidgetItem("12:30 PM"))
                self.roomSchedule.setItem(10, 0, QTableWidgetItem("1:00 PM"))
                self.roomSchedule.setItem(11, 0, QTableWidgetItem("1:30 PM"))
                self.roomSchedule.setItem(12, 0, QTableWidgetItem("2:00 PM"))
                self.roomSchedule.setItem(13, 0, QTableWidgetItem("2:30 PM"))
                self.roomSchedule.setItem(14, 0, QTableWidgetItem("3:00 PM"))
                self.roomSchedule.setItem(15, 0, QTableWidgetItem("3:30 PM"))
                self.roomSchedule.setItem(16, 0, QTableWidgetItem("4:00 PM"))
                self.roomSchedule.setItem(17, 0, QTableWidgetItem("4:30 PM"))
                self.roomSchedule.setItem(18, 0, QTableWidgetItem("5:00 PM"))
                self.roomSchedule.setItem(19, 0, QTableWidgetItem("5:30 PM"))
                self.roomSchedule.setItem(20, 0, QTableWidgetItem("6:00 PM"))
                self.roomSchedule.setItem(21, 0, QTableWidgetItem("6:30 PM"))
                self.roomSchedule.setItem(22, 0, QTableWidgetItem("7:00 PM"))
                self.roomSchedule.setItem(23, 0, QTableWidgetItem("7:30 PM"))
                self.roomSchedule.setItem(24, 0, QTableWidgetItem("8:00 PM"))
                self.roomSchedule.setItem(25, 0, QTableWidgetItem("8:30 PM"))

                self.roomSchedule.setItem(0, 1, QTableWidgetItem("Monday"))
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
                self.roomSchedule.setItem(15, 1, QTableWidgetItem())
                self.roomSchedule.setItem(16, 1, QTableWidgetItem())
                self.roomSchedule.setItem(17, 1, QTableWidgetItem())
                self.roomSchedule.setItem(18, 1, QTableWidgetItem())
                self.roomSchedule.setItem(19, 1, QTableWidgetItem())
                self.roomSchedule.setItem(20, 1, QTableWidgetItem())
                self.roomSchedule.setItem(21, 1, QTableWidgetItem())
                self.roomSchedule.setItem(22, 1, QTableWidgetItem())
                self.roomSchedule.setItem(23, 1, QTableWidgetItem())
                self.roomSchedule.setItem(24, 1, QTableWidgetItem())
                self.roomSchedule.setItem(25, 1, QTableWidgetItem())

                self.roomSchedule.setItem(0, 2, QTableWidgetItem("Tuesday"))
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
                self.roomSchedule.setItem(15, 2, QTableWidgetItem())
                self.roomSchedule.setItem(16, 2, QTableWidgetItem())
                self.roomSchedule.setItem(17, 2, QTableWidgetItem())
                self.roomSchedule.setItem(18, 2, QTableWidgetItem())
                self.roomSchedule.setItem(19, 2, QTableWidgetItem())
                self.roomSchedule.setItem(20, 2, QTableWidgetItem())
                self.roomSchedule.setItem(21, 2, QTableWidgetItem())
                self.roomSchedule.setItem(22, 2, QTableWidgetItem())
                self.roomSchedule.setItem(23, 2, QTableWidgetItem())
                self.roomSchedule.setItem(24, 2, QTableWidgetItem())
                self.roomSchedule.setItem(25, 2, QTableWidgetItem())

                self.roomSchedule.setItem(0, 3, QTableWidgetItem("Wednesday"))
                self.roomSchedule.setItem(1, 3, QTableWidgetItem())
                self.roomSchedule.setItem(2, 3, QTableWidgetItem())
                self.roomSchedule.setItem(3, 3, QTableWidgetItem())
                self.roomSchedule.setItem(4, 3, QTableWidgetItem())
                self.roomSchedule.setItem(5, 3, QTableWidgetItem())
                self.roomSchedule.setItem(6, 3, QTableWidgetItem())
                self.roomSchedule.setItem(7, 3, QTableWidgetItem())
                self.roomSchedule.setItem(8, 3, QTableWidgetItem())
                self.roomSchedule.setItem(9, 3, QTableWidgetItem())
                self.roomSchedule.setItem(10,3, QTableWidgetItem())
                self.roomSchedule.setItem(11, 3, QTableWidgetItem())
                self.roomSchedule.setItem(12, 3, QTableWidgetItem())
                self.roomSchedule.setItem(13, 3, QTableWidgetItem())
                self.roomSchedule.setItem(14, 3, QTableWidgetItem())
                self.roomSchedule.setItem(15, 3, QTableWidgetItem())
                self.roomSchedule.setItem(16, 3, QTableWidgetItem())
                self.roomSchedule.setItem(17, 3, QTableWidgetItem())
                self.roomSchedule.setItem(18, 3, QTableWidgetItem())
                self.roomSchedule.setItem(19, 3, QTableWidgetItem())
                self.roomSchedule.setItem(20, 3, QTableWidgetItem())
                self.roomSchedule.setItem(21, 3, QTableWidgetItem())
                self.roomSchedule.setItem(22, 3, QTableWidgetItem())
                self.roomSchedule.setItem(23, 3, QTableWidgetItem())
                self.roomSchedule.setItem(24, 3, QTableWidgetItem())
                self.roomSchedule.setItem(25, 3, QTableWidgetItem())

                self.roomSchedule.setItem(0, 4, QTableWidgetItem("Thursday"))
                self.roomSchedule.setItem(1, 4, QTableWidgetItem())
                self.roomSchedule.setItem(2, 4, QTableWidgetItem())
                self.roomSchedule.setItem(3, 4, QTableWidgetItem())
                self.roomSchedule.setItem(4, 4, QTableWidgetItem())
                self.roomSchedule.setItem(5, 4, QTableWidgetItem())
                self.roomSchedule.setItem(6, 4, QTableWidgetItem())
                self.roomSchedule.setItem(7, 4, QTableWidgetItem())
                self.roomSchedule.setItem(8, 4, QTableWidgetItem())
                self.roomSchedule.setItem(9, 4, QTableWidgetItem())
                self.roomSchedule.setItem(10,4, QTableWidgetItem())
                self.roomSchedule.setItem(11, 4, QTableWidgetItem())
                self.roomSchedule.setItem(12, 4, QTableWidgetItem())
                self.roomSchedule.setItem(13, 4, QTableWidgetItem())
                self.roomSchedule.setItem(14, 4, QTableWidgetItem())
                self.roomSchedule.setItem(15, 4, QTableWidgetItem())
                self.roomSchedule.setItem(16, 4, QTableWidgetItem())
                self.roomSchedule.setItem(17, 4, QTableWidgetItem())
                self.roomSchedule.setItem(18, 4, QTableWidgetItem())
                self.roomSchedule.setItem(19, 4, QTableWidgetItem())
                self.roomSchedule.setItem(20, 4, QTableWidgetItem())
                self.roomSchedule.setItem(21, 4, QTableWidgetItem())
                self.roomSchedule.setItem(22, 4, QTableWidgetItem())
                self.roomSchedule.setItem(23, 4, QTableWidgetItem())
                self.roomSchedule.setItem(24, 4, QTableWidgetItem())
                self.roomSchedule.setItem(25, 4, QTableWidgetItem())

                #print("list of rooms", self.listofRooms)
                #for i in self.listofRooms:
                #print(type(i))
                '''[room[week[day]]]'''

                roomLists = []

                for j in self.listofRooms:
                        if (j == ""):
                                pass
                        else:
                               #print(j.__str__())
                              # print(j.schedule)
                               roomLists.append(j.__str__())
                               #roomLists.append(j.schedule)
                               w = 0
                               for week in j.schedule:
                                        if int((self.weekIndex-1)) == w:
                                             roomLists.append(week)
                                             #print(week)
                                             w+=1
                                        else:
                                               w+=1
                                               #print("skipped")

                #print(self.weekIndex-1)       
                #print(roomLists)

                listToUse = []
                #print()

                for room in roomLists: 
                       if type(room) == str:
                              listToUse.append(room)
                              #print(room)
                              dayC = 0
                       else:
                                weekList = []
                                for week1 in room: 
                                        dayC +=1
                                        weekList.append(dayC)
                                        for day in week1:
                                                if type(day) == str:
                                                        #print(day, self.cohortText)
                                                        weekList.append(day)
                                                        #print(self.cohortText, day)
                                                else:
                                                       weekList.append(day)
                                                       #print("it is none")
                                listToUse.append(weekList)

                #print(listToUse)
                #print()

                listActual = []
                for week2 in listToUse:
                        if type(week2) == str:
                                listActual.append(week2)
                        else:
                                listed = []
                                for i in week2:
                                        if type(i) == int or type(i) != str:
                                                listed.append(i)
                                                #print("it is none type or int")
                                        else:
                                                if i.rfind(self.cohortText) != -1:
                                                        listed.append(i)
                                                        #print(i)
                                                else:
                                                       listed.append(None)
                                                       #print("it is none type or int")
                                listActual.append(listed)
                #we now have a list of lists of the speicific week in each room for the cohort
                #print(listActual)
                #print()

                listToUse2 = [[1, None, None, None, None, None,None,None, None,None,None, None,None,None, None,None,None, None,None, None, None, None, None, None,None,None, None]
                               ,[2,None, None, None, None, None,None,None, None,None,None, None,None,None, None,None,None, None,None, None, None, None, None, None,None,None, None]
                               ,[3,None, None, None, None, None,None,None, None,None,None, None,None,None, None,None,None, None,None, None, None, None, None, None,None,None, None] 
                               ,[4,None, None, None, None, None,None,None, None,None,None, None,None,None, None,None,None, None,None, None, None, None, None, None,None,None, None]]

                
                tempList = ['Room 1',[1, 'PCOM_0203 / BCOM21', 'PCOM_0203 / BCOM21', 'PCOM_0203 / BCOM21', None, None, 'PCOM_0203 / BCOM21', None, None, None, 'PCOM_0203 / BCOM21', 'PCOM_0203 / BCOM21', None, None, None, None, 'PCOM_0203 / BCOM21', None, None, 
                             2,None, None, 'PCOM_0203 / BCOM21', 'PCOM_0203 / BCOM21', None, None, 'PCOM_0203 / BCOM21', 'PCOM_0203 / BCOM21', 'PCOM_0203 / BCOM21', None, None, None, None, None, None, None, None, 'PCOM_0203 / BCOM21',
                             3,'PCOM_0203 / BCOM21', 'PCOM_0203 / BCOM21', 'PCOM_0203 / BCOM21', None, None,'PCOM_0203 / BCOM21', None, None, None, 'PCOM_0203 / BCOM21', 'PCOM_0203 / BCOM21', None, None, None, None, 'PCOM_0203 / BCOM21', None, None,
                             4, None, None, 'PCOM_0203 / BCOM21', 'PCOM_0203 / BCOM21', None, None, 'PCOM_0203 / BCOM21', 'PCOM_0203 / BCOM21', 'PCOM_0203 / BCOM21', None, None, None, None, None, None, None, None, 'PCOM_0203 / BCOM21'],
                             'Room 2',[1, None, None, None, 'PCOM_0203 / BCOM21', None,None,None, 'PCOM_0203 / BCOM21',None,None, None,'PCOM_0203 / BCOM21', 'PCOM_0203 / BCOM21', 'PCOM_0203 / BCOM21',None,None, None,None, 'PCOM_0203 / BCOM21', 'PCOM_0203 / BCOM21', None, None, 'PCOM_0203 / BCOM21',None,None, None, 
                               2,'PCOM_0203 / BCOM21', None, None, None, 'PCOM_0203 / BCOM21','PCOM_0203 / BCOM21',None, None,None,None, 'PCOM_0203 / BCOM21', 'PCOM_0203 / BCOM21', 'PCOM_0203 / BCOM21', None,None,None, None,None, 'PCOM_0203 / BCOM21', 'PCOM_0203 / BCOM21', None, None, 'PCOM_0203 / BCOM21', 'PCOM_0203 / BCOM21',None, None,
                               3,None, None, None, 'PCOM_0203 / BCOM21', None,None,None, 'PCOM_0203 / BCOM21',None,None, None,'PCOM_0203 / BCOM21', 'PCOM_0203 / BCOM21', 'PCOM_0203 / BCOM21',None,None, None,None, 'PCOM_0203 / BCOM21', 'PCOM_0203 / BCOM21', None, None, 'PCOM_0203 / BCOM21',None,None, None,
                               4,'PCOM_0203 / BCOM21', None, None, None, 'PCOM_0203 / BCOM21','PCOM_0203 / BCOM21',None, None,None,None, 'PCOM_0203 / BCOM21', 'PCOM_0203 / BCOM21', 'PCOM_0203 / BCOM21', None,None,None, None,None, 'PCOM_0203 / BCOM21', 'PCOM_0203 / BCOM21', None, None, 'PCOM_0203 / BCOM21', 'PCOM_0203 / BCOM21',None, None]]
                '''
                tempList = ['Room 1',[1, 'PCOM_0203 / BCOM21', 'PCOM_0203 / BCOM21', 'PCOM_0203 / BCOM21', None, None, 'PCOM_0203 / BCOM21', None, None, None, 'PCOM_0203 / BCOM21', 'PCOM_0203 / BCOM21', None, None, None, None, 'PCOM_0203 / BCOM21', None, None, 
                             2,None, None, 'PCOM_0203 / BCOM21', 'PCOM_0203 / BCOM21', None, None, 'PCOM_0203 / BCOM21', 'PCOM_0203 / BCOM21', 'PCOM_0203 / BCOM21', None, None, None, None, None, None, None, None, 'PCOM_0203 / BCOM21',
                             3,'PCOM_0203 / BCOM21', 'PCOM_0203 / BCOM21', 'PCOM_0203 / BCOM21', None, None,'PCOM_0203 / BCOM21', None, None, None, 'PCOM_0203 / BCOM21', 'PCOM_0203 / BCOM21', None, None, None, None, 'PCOM_0203 / BCOM21', None, None,
                             4, None, None, 'PCOM_0203 / BCOM21', 'PCOM_0203 / BCOM21', None, None, 'PCOM_0203 / BCOM21', 'PCOM_0203 / BCOM21', 'PCOM_0203 / BCOM21', None, None, None, None, None, None, None, None, 'PCOM_0203 / BCOM21']]
                '''

                roomNumber = ""
                daytoAddTo = 0
                for weeks5 in listActual:
                       if type(weeks5) == str:
                              roomNumber = weeks5
                              daytoAddTo = 0
                       else:
                              if daytoAddTo > 4:
                                      break
                              else:
                                indexToAddTo = 0
                                for slot in weeks5:
                                                if type(slot) == int:
                                                        #print("its a number, time resetted")
                                                        indexToAddTo = 0
                                                        daytoAddTo += 1
                                                else:
                                                        if type(slot) == str:
                                                                slotSplit = slot.split()
                                                                courseToAdd = slotSplit[0] + " / " + roomNumber
                                                                #print(courseToAdd)
                                                                #print("index to add to: ", indexToAddTo,slot, daytoAddTo)
                                                                for insideList in listToUse2:
                                                                        if insideList[0] == daytoAddTo:
                                                                                insideList[indexToAddTo+1] = courseToAdd
                                                                indexToAddTo+=1
                                                        else:
                                                                indexToAddTo+=1

                #print(listToUse2)
                #print()

                finalList = []
                for i in listToUse2:
                       for j in i:
                              finalList.append(j)

                #print(finalList)

                row = 1
                coloumn = 1
                list3 = []


                for course2 in finalList:
                        if (type(course2) == int) :
                                if (course2 == 1):
                                        #print("day change", course2, coloumn)
                                        pass
                                else:
                                        #print("day change", course2, coloumn)
                                        coloumn+=1
                                        row = 1
                                        list3.clear()

                        else:
                                if (str(course2) == "None"):
                                        row+=1
                                else:
                                        if (len(list3)== 0):
                                                list3.append(str(course2))
                                                #setting colors
                                                color = tuple(random.choices(range(256), k=3))
                                                #print("color", color)
                                                firstNum = color[0]
                                                secondNum = color[1]
                                                thirdNum = color[2]
                                                self.roomSchedule.setItem(row,coloumn, QTableWidgetItem(str(course2)))
                                                self.roomSchedule.item(row, coloumn).setBackground(QColor(firstNum,secondNum,thirdNum))
                                                row+=1
                                                #print(course2)
                                        else:
                                                if (str(course2) in list3):
                                                        #printing course
                                                        self.roomSchedule.setItem(row,coloumn, QTableWidgetItem(str(course2)))
                                                        self.roomSchedule.item(row, coloumn).setBackground(QColor(firstNum,secondNum,thirdNum))
                                                        #incrementing
                                                        row+=1
                                                        #print(course2)
                                                else:
                                                        list3.append(str(course2))
                                                        #setting colors
                                                        color = tuple(random.choices(range(256), k=3))
                                                        #print("color", color)
                                                        firstNum = color[0]
                                                        secondNum = color[1]
                                                        thirdNum = color[2]
                                                        #printing course
                                                        self.roomSchedule.setItem(row,coloumn, QTableWidgetItem(str(course2)))
                                                        self.roomSchedule.item(row, coloumn).setBackground(QColor(firstNum,secondNum,thirdNum))
                                                        #incrementing
                                                        row+=1
                                                        #print(course2)  

        elif self.ctext != "":
                #print("week index: ", self.weekIndex)
                self.roomSchedule.clearContents()
                self.roomSchedule.setItem(0, 0, QTableWidgetItem("Time"))
                self.roomSchedule.setItem(1, 0, QTableWidgetItem("8:00 AM"))
                self.roomSchedule.setItem(2, 0, QTableWidgetItem("8:30 AM"))
                self.roomSchedule.setItem(3, 0, QTableWidgetItem("9:00 AM"))
                self.roomSchedule.setItem(4, 0, QTableWidgetItem("9:30 AM"))
                self.roomSchedule.setItem(5, 0, QTableWidgetItem("10:30 AM"))
                self.roomSchedule.setItem(6, 0, QTableWidgetItem("11:00 AM"))
                self.roomSchedule.setItem(7, 0, QTableWidgetItem("11:30 AM"))
                self.roomSchedule.setItem(8, 0, QTableWidgetItem("12:00 PM"))
                self.roomSchedule.setItem(9, 0, QTableWidgetItem("12:30 PM"))
                self.roomSchedule.setItem(10, 0, QTableWidgetItem("1:00 PM"))
                self.roomSchedule.setItem(11, 0, QTableWidgetItem("1:30 PM"))
                self.roomSchedule.setItem(12, 0, QTableWidgetItem("2:00 PM"))
                self.roomSchedule.setItem(13, 0, QTableWidgetItem("2:30 PM"))
                self.roomSchedule.setItem(14, 0, QTableWidgetItem("3:00 PM"))
                self.roomSchedule.setItem(15, 0, QTableWidgetItem("3:30 PM"))
                self.roomSchedule.setItem(16, 0, QTableWidgetItem("4:00 PM"))
                self.roomSchedule.setItem(17, 0, QTableWidgetItem("4:30 PM"))
                self.roomSchedule.setItem(18, 0, QTableWidgetItem("5:00 PM"))
                self.roomSchedule.setItem(19, 0, QTableWidgetItem("5:30 PM"))
                self.roomSchedule.setItem(20, 0, QTableWidgetItem("6:00 PM"))
                self.roomSchedule.setItem(21, 0, QTableWidgetItem("6:30 PM"))
                self.roomSchedule.setItem(22, 0, QTableWidgetItem("7:00 PM"))
                self.roomSchedule.setItem(23, 0, QTableWidgetItem("7:30 PM"))
                self.roomSchedule.setItem(24, 0, QTableWidgetItem("8:00 PM"))
                self.roomSchedule.setItem(25, 0, QTableWidgetItem("8:30 PM"))

                self.roomSchedule.setItem(0, 1, QTableWidgetItem("Monday"))
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
                self.roomSchedule.setItem(15, 1, QTableWidgetItem())
                self.roomSchedule.setItem(16, 1, QTableWidgetItem())
                self.roomSchedule.setItem(17, 1, QTableWidgetItem())
                self.roomSchedule.setItem(18, 1, QTableWidgetItem())
                self.roomSchedule.setItem(19, 1, QTableWidgetItem())
                self.roomSchedule.setItem(20, 1, QTableWidgetItem())
                self.roomSchedule.setItem(21, 1, QTableWidgetItem())
                self.roomSchedule.setItem(22, 1, QTableWidgetItem())
                self.roomSchedule.setItem(23, 1, QTableWidgetItem())
                self.roomSchedule.setItem(24, 1, QTableWidgetItem())
                self.roomSchedule.setItem(25, 1, QTableWidgetItem())

                self.roomSchedule.setItem(0, 2, QTableWidgetItem("Tuesday"))
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
                self.roomSchedule.setItem(15, 2, QTableWidgetItem())
                self.roomSchedule.setItem(16, 2, QTableWidgetItem())
                self.roomSchedule.setItem(17, 2, QTableWidgetItem())
                self.roomSchedule.setItem(18, 2, QTableWidgetItem())
                self.roomSchedule.setItem(19, 2, QTableWidgetItem())
                self.roomSchedule.setItem(20, 2, QTableWidgetItem())
                self.roomSchedule.setItem(21, 2, QTableWidgetItem())
                self.roomSchedule.setItem(22, 2, QTableWidgetItem())
                self.roomSchedule.setItem(23, 2, QTableWidgetItem())
                self.roomSchedule.setItem(24, 2, QTableWidgetItem())
                self.roomSchedule.setItem(25, 2, QTableWidgetItem())

                self.roomSchedule.setItem(0, 3, QTableWidgetItem("Wednesday"))
                self.roomSchedule.setItem(1, 3, QTableWidgetItem())
                self.roomSchedule.setItem(2, 3, QTableWidgetItem())
                self.roomSchedule.setItem(3, 3, QTableWidgetItem())
                self.roomSchedule.setItem(4, 3, QTableWidgetItem())
                self.roomSchedule.setItem(5, 3, QTableWidgetItem())
                self.roomSchedule.setItem(6, 3, QTableWidgetItem())
                self.roomSchedule.setItem(7, 3, QTableWidgetItem())
                self.roomSchedule.setItem(8, 3, QTableWidgetItem())
                self.roomSchedule.setItem(9, 3, QTableWidgetItem())
                self.roomSchedule.setItem(10,3, QTableWidgetItem())
                self.roomSchedule.setItem(11, 3, QTableWidgetItem())
                self.roomSchedule.setItem(12, 3, QTableWidgetItem())
                self.roomSchedule.setItem(13, 3, QTableWidgetItem())
                self.roomSchedule.setItem(14, 3, QTableWidgetItem())
                self.roomSchedule.setItem(15, 3, QTableWidgetItem())
                self.roomSchedule.setItem(16, 3, QTableWidgetItem())
                self.roomSchedule.setItem(17, 3, QTableWidgetItem())
                self.roomSchedule.setItem(18, 3, QTableWidgetItem())
                self.roomSchedule.setItem(19, 3, QTableWidgetItem())
                self.roomSchedule.setItem(20, 3, QTableWidgetItem())
                self.roomSchedule.setItem(21, 3, QTableWidgetItem())
                self.roomSchedule.setItem(22, 3, QTableWidgetItem())
                self.roomSchedule.setItem(23, 3, QTableWidgetItem())
                self.roomSchedule.setItem(24, 3, QTableWidgetItem())
                self.roomSchedule.setItem(25, 3, QTableWidgetItem())

                self.roomSchedule.setItem(0, 4, QTableWidgetItem("Thursday"))
                self.roomSchedule.setItem(1, 4, QTableWidgetItem())
                self.roomSchedule.setItem(2, 4, QTableWidgetItem())
                self.roomSchedule.setItem(3, 4, QTableWidgetItem())
                self.roomSchedule.setItem(4, 4, QTableWidgetItem())
                self.roomSchedule.setItem(5, 4, QTableWidgetItem())
                self.roomSchedule.setItem(6, 4, QTableWidgetItem())
                self.roomSchedule.setItem(7, 4, QTableWidgetItem())
                self.roomSchedule.setItem(8, 4, QTableWidgetItem())
                self.roomSchedule.setItem(9, 4, QTableWidgetItem())
                self.roomSchedule.setItem(10,4, QTableWidgetItem())
                self.roomSchedule.setItem(11, 4, QTableWidgetItem())
                self.roomSchedule.setItem(12, 4, QTableWidgetItem())
                self.roomSchedule.setItem(13, 4, QTableWidgetItem())
                self.roomSchedule.setItem(14, 4, QTableWidgetItem())
                self.roomSchedule.setItem(15, 4, QTableWidgetItem())
                self.roomSchedule.setItem(16, 4, QTableWidgetItem())
                self.roomSchedule.setItem(17, 4, QTableWidgetItem())
                self.roomSchedule.setItem(18, 4, QTableWidgetItem())
                self.roomSchedule.setItem(19, 4, QTableWidgetItem())
                self.roomSchedule.setItem(20, 4, QTableWidgetItem())
                self.roomSchedule.setItem(21, 4, QTableWidgetItem())
                self.roomSchedule.setItem(22, 4, QTableWidgetItem())
                self.roomSchedule.setItem(23, 4, QTableWidgetItem())
                self.roomSchedule.setItem(24, 4, QTableWidgetItem())
                self.roomSchedule.setItem(25, 4, QTableWidgetItem())


                #print("list of rooms", self.listofRooms)
                #for i in self.listofRooms:
                #print(type(i))

                for j in self.listofRooms:
                        if (j == ""):
                                pass
                        else:
                                if j.room_number == self.ctext:
                                        weeklist = []
                                        w = 0
                                        #print(j.schedule)
                                        for week in j.schedule:
                                                w += 1
                                                d = 0
                                                co = 0
                                                weekdayList = []
                                                for weekday in week:
                                                        weekdayList.append(weekday)
                                                        co+=1
                                                        d += 1
                                                weeklist.append(weekdayList)


                #print("weekList", weeklist)
                #print (weeklist[0][0][0]) #gives class name
                #print (weeklist[0][0]) # gives weekday mon, tues wed or thurs
                #print (weeklist[0]) #gives all weekdays in a week

                #setting class schedule
                #lectures: 18
                #labs: 25
                listToUse = []

                #taking a week's schedule and putting it in list to read from
                countDay = 0
                for week2 in weeklist[self.weekIndex-1]:
                        #print(week2)
                        #print("week# changed", week2)
                        countDay +=1
                        listToUse.append(countDay)
                        counterSlot = len(week2)+1
                        for course in week2:
                                #print("course", type(course), course)
                                listToUse.append(course)

                #print("list to use", listToUse)


                '''color randomizer code'''
                #color = tuple(random.choices(range(256), k=3))
                #print("color", color)
                
                row = 1
                coloumn = 1
                list3 = []


                for course2 in listToUse:
                        if (type(course2) == int) :
                                if (course2 == 1):
                                        #print("day change", course2, coloumn)
                                        pass
                                else:
                                        #print("day change", course2, coloumn)
                                        coloumn+=1
                                        row = 1
                                        list3.clear()

                        else:
                                if (str(course2) == "None"):
                                        row+=1
                                else:
                                        if (len(list3)== 0):
                                                list3.append(str(course2))
                                                #setting colors
                                                color = tuple(random.choices(range(256), k=3))
                                                #print("color", color)
                                                firstNum = color[0]
                                                secondNum = color[1]
                                                thirdNum = color[2]
                                                self.roomSchedule.setItem(row,coloumn, QTableWidgetItem(str(course2)))
                                                self.roomSchedule.item(row, coloumn).setBackground(QColor(firstNum,secondNum,thirdNum))
                                                row+=1
                                                #print(course2)
                                        else:
                                                if (str(course2) in list3):
                                                        #printing course
                                                        self.roomSchedule.setItem(row,coloumn, QTableWidgetItem(str(course2)))
                                                        self.roomSchedule.item(row, coloumn).setBackground(QColor(firstNum,secondNum,thirdNum))
                                                        #incrementing
                                                        row+=1
                                                        #print(course2)
                                                else:
                                                        list3.append(str(course2))
                                                        #setting colors
                                                        color = tuple(random.choices(range(256), k=3))
                                                        #print("color", color)
                                                        firstNum = color[0]
                                                        secondNum = color[1]
                                                        thirdNum = color[2]
                                                        #printing course
                                                        self.roomSchedule.setItem(row,coloumn, QTableWidgetItem(str(course2)))
                                                        self.roomSchedule.item(row, coloumn).setBackground(QColor(firstNum,secondNum,thirdNum))
                                                        #incrementing
                                                        row+=1
                                                        #print(course2)



'''Mon: [PCOM_0101, PCOM_0101, PCOM_0101, PCOM_0105, PCOM_0105, PCOM_0105, None, None, None, None, None, None, None, None, None, None, None, None]
        Tue: [PRDV_0640, PRDV_0640, PRDV_0640, PRDV_0652, PRDV_0652, PRDV_0652, PRDV_0653, PRDV_0653, PRDV_0653, PRDV_0642, PRDV_0642, PRDV_0642, None, None, None, None, None, None]
        Wed: [PCOM_0101, PCOM_0101, PCOM_0101, PCOM_0105, PCOM_0105, PCOM_0105, None, None, None, None, None, None, None, None, None, None, None, None]
        Thu: [PRDV_0640, PRDV_0640, PRDV_0640, PRDV_0652, PRDV_0652, PRDV_0652, PRDV_0653, PRDV_0653, PRDV_0653, PRDV_0642, PRDV_0642, PRDV_0642, None, None, None, None, None, None]'''


# if __name__ == "__main__":
#     #first schedule builder window
#     App = QApplication(sys.argv)
#     window = webapp.MainWindow()
#     #start the event loop
#     App.exec()

#     App = QApplication(sys.argv)
#     window = MainWindow2()
#     #start the event loop
#     App.exec()
#     print("hello")

