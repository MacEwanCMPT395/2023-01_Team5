import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import settingText
import pandas as pd
import data_structures as dataStruc

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        '''making the schedule builder window'''
        self.acceptDrops()
        self.setWindowTitle("Schedule Builder")
        self.setGeometry(0, 0, 1900, 835) # x,y,w,h
        self.setFixedSize(QSize(1900, 835)) # w,h
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
        self.label1.move(20,340)

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
        self.roomNumber.addItems(["", dataStruc.Computer_Lab.room_number])
        self.roomNumber.activated.connect(self.roomChosen)

        '''week combo box'''
        self.weekLabel = QLabel("Week Number:",self)
        self.weekLabel.move (20,220)
        self.weekLabel.resize(200,30)
        self.weekLabel.setFont(QFont('Arial',12))
        self.weekLabel.setStyleSheet("QLabel { color : #902a39; }; font-weight: bold")
        self.weekNumber = QComboBox(self)
        self.weekNumber.move(190,220)
        self.weekNumber.resize(190,35)
        self.weekNumber.addItems(["", "1:(Sept 4-10)", "2: (Sept 11-17)", "3: (Sept 18-24)", "4: (Sept 25-Oct 1)", "5: (Oct 2-8)", 
                    "6: (Oct 9-15)", "7: (Oct 16-22)", "8: (Oct 23-28)", "9: (Oct 29-Nov 4)", "10: (Nov 5-11)","11: (Nov 12-18)",
                    "11: (Nov 12-18)", "12: (Nov 19-25)", "13: (Nov 26-Dec 2)", "14: (Dec 3-9)"])
        self.weekNumber.activated.connect(self.weekChosen)

        '''making the export button'''
        self.export = QPushButton("EXPORT", self)
        self.export.setGeometry(200,305,175,25)
        self.export.setStyleSheet("QPushButton {background-color: #902a39; color: white}")
        #self.submit.clicked.connect(self.clickExport)

        '''making the redo button'''
        self.redo = QPushButton("START OVER", self)
        self.redo.setGeometry(20,305,175,25)
        self.redo.setStyleSheet("QPushButton {background-color: #902a39; color: white}")
        #self.submit.clicked.connect(self.clickRedo)

        '''making the submit button'''
        self.submit = QPushButton("SUBMIT", self)
        self.submit.setGeometry(20,270,355,25)
        self.submit.setStyleSheet("QPushButton {background-color: #902a39; color: white}")
        self.submit.clicked.connect(self.clickSubmit)
        #355,462

        '''table stuff'''
        self.roomSchedule = QTableWidget(self)
        self.roomSchedule.move(400,150)
        self.roomSchedule.resize(1475,657)
        self.roomSchedule.setStyleSheet("border: 2px solid black; font-weight: bold")
        #self.roomSchedule.setAlignment(QtCore.Qt.AlignCenter) 

        # Giving the count for the Row   
        self.roomSchedule.setRowCount(26)  
    
        # Giving the count for the Column  
        self.roomSchedule.setColumnCount(3)  
    
        #initializing the coloumns and rows
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

        #making the coloumns,rows, tables look pretty
        self.roomSchedule.verticalHeader().hide()
        self.roomSchedule.horizontalHeader().hide()
        self.roomSchedule.setColumnWidth(0, 100)
        self.roomSchedule.setColumnWidth(1,670)
        self.roomSchedule.setColumnWidth(2,670)

        dataStruc.Computer_Lab.update_schedule(dataStruc.CMSK_0150, 0, 0, 0, 1)
        dataStruc.Computer_Lab.update_schedule(dataStruc.ACCT_0202, 0, 1, 0, 2)
        dataStruc.Computer_Lab.update_schedule(dataStruc.DXDI_0101, 0, 0, 3, 3)
        #dataStruc.Computer_Lab.print_schedule()

        '''showing the initial screen'''
        self.show()
    
    def roomChosen(self,index):
        self.ctext = self.roomNumber.itemText(index)  # Get the text at index.
        self.roomIndex = self.roomNumber.currentIndex()
        
    def weekChosen(self,index):
        self.wtext = self.weekNumber.itemText(index)  # Get the text at index.
        self.weekIndex = self.weekNumber.currentIndex()
        
    def clickSubmit(self):
        #ctext = self.roomNumber.itemText(index)  # Get the text at index.
        #print("Current itemText", ctext)
        fallDict = {1:"(Sept 4-10)", 2: "(Sept 11-17)", 3: "(Sept 18-24)", 4: "(Sept 25-Oct 1)", 5: "(Oct 2-8)", 
                    6: "(Oct 9-15)", 7: "(Oct 16-22)", 8: "(Oct 23-2)"}
        
        #print("Current room selected", self.ctext)
        #print("Current room selected", self.wtext)
        print("week index: ", self.weekIndex)
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
        
        weeklist = []
        w = 0
        for week in dataStruc.Computer_Lab.schedule:
                w += 1
                d = 0
                co = 0
                weekdayList = []
                for weekday in week:
                        weekdayList.append(weekday)
                        co+=1
                        d += 1
                weeklist.append(weekdayList)

        #print(weeklist)
        #print (weeklist[0][0][0]) #gives class name
        #print (weeklist[0][0]) # gives weekday mon, tues wed or thurs
        #print (weeklist[0]) #gives all weekdays in a week

        #setting class schedule
        class1 = ""
        nextClass = ""
        colorList = ["darkRed", "yellow",  "green", "cyan", "purple", "gray", "brown"]
        row = 1
        coloumn = 1
        checkClass = False
        count = 0
        colorChoice = 0

        for week2 in weeklist[self.weekIndex-1]:
                #print ("hi",week2)
                class1 = str(week2[0])
                nextClass = str(week2[1])
                #print("a",class1)
                #print("b", nextClass)
                count = 0
                checkClass = False
                for day2 in week2[1:]:
                        if (nextClass == class1):
                                class1 = nextClass
                                nextClass = str(day2)
                                count += 1
                        else:
                                #print ("count", count)
                                if checkClass == True:
                                        if nextClass == "None":
                                                count +=1
                                                checkClass = False
                                count2 = 0
                                self.roomSchedule.setItem(row,coloumn, QTableWidgetItem(class1))
                                while (count2 < count):
                                        self.roomSchedule.item(row, coloumn).setBackground(QColor(colorList[colorChoice])) #row, coloumn
                                        row += 1
                                        count2+=1
                                colorChoice += 1
                                count = 0
                                class1 = nextClass
                                nextClass = str(day2)
                                #print("now", nextClass)
                                checkClass = True                                     
                #print ("hell",week2)
                if coloumn == 2:
                        break
                else:
                        coloumn +=1
                        row = 1

        
        


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = MainWindow()
    #start the event loop
    App.exec()
    print("hello")

    ''' 
        15 weeks
        11-532
Week 1:
Mon: [CMSK_0150, CMSK_0150, CMSK_0150, DXDI_0101, DXDI_0101, DXDI_0101, DXDI_0101, DXDI_0101, DXDI_0101, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
Tue: [ACCT_0202, ACCT_0202, ACCT_0202, ACCT_0202, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
Wed: [CMSK_0150, CMSK_0150, CMSK_0150, DXDI_0101, DXDI_0101, DXDI_0101, DXDI_0101, DXDI_0101, DXDI_0101, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
Thu: [ACCT_0202, ACCT_0202, ACCT_0202, ACCT_0202, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
Week 2:
Mon: [CMSK_0150, CMSK_0150, CMSK_0150, DXDI_0101, DXDI_0101, DXDI_0101, DXDI_0101, DXDI_0101, DXDI_0101, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
Tue: [ACCT_0202, ACCT_0202, ACCT_0202, ACCT_0202, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
Wed: [CMSK_0150, CMSK_0150, CMSK_0150, DXDI_0101, DXDI_0101, DXDI_0101, DXDI_0101, DXDI_0101, DXDI_0101, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
Thu: [ACCT_0202, ACCT_0202, ACCT_0202, ACCT_0202, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
Week 3:
Mon: [CMSK_0150, CMSK_0150, CMSK_0150, DXDI_0101, DXDI_0101, DXDI_0101, DXDI_0101, DXDI_0101, DXDI_0101, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
Tue: [ACCT_0202, ACCT_0202, ACCT_0202, ACCT_0202, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
Wed: [CMSK_0150, CMSK_0150, CMSK_0150, DXDI_0101, DXDI_0101, DXDI_0101, DXDI_0101, DXDI_0101, DXDI_0101, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
Thu: [ACCT_0202, ACCT_0202, ACCT_0202, ACCT_0202, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
Week 4:
Mon: [CMSK_0150, CMSK_0150, CMSK_0150, DXDI_0101, DXDI_0101, DXDI_0101, DXDI_0101, DXDI_0101, DXDI_0101, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
Tue: [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
Wed: [CMSK_0150, CMSK_0150, CMSK_0150, DXDI_0101, DXDI_0101, DXDI_0101, DXDI_0101, DXDI_0101, DXDI_0101, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
Thu: [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
Week 5:
Mon: [CMSK_0150, CMSK_0150, CMSK_0150, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
Tue: [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
Wed: [CMSK_0150, CMSK_0150, CMSK_0150, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
Thu: [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
Week 6:
Mon: [CMSK_0150, CMSK_0150, CMSK_0150, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
Tue: [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
Wed: [CMSK_0150, CMSK_0150, CMSK_0150, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
Thu: [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
Week 7:
Mon: [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
Tue: [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
Wed: [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
Thu: [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
        '''