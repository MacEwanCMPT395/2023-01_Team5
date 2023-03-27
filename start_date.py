import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Start_Date(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(QSize(200, 200)) # w,h
        self.calendar()
        self.week_number = []
    def calendar(self):
        #create label
        label = QLabel("Please enter semester start date:", self)
        label.setGeometry(50, 10, 100, 75)
        label.setAlignment(QtCore.Qt.AlignCenter)
        label.setFont(QFont('Times', 12))
        # making label multiline
        label.setWordWrap(True)


        self.dateedit = QtWidgets.QDateEdit(self, calendarPopup=True)
        self.dateedit.setGeometry(50, 100, 100, 20)
        self.dateedit.setDateTime(QtCore.QDateTime.currentDateTime())

        self.submit = QPushButton("Submit", self)
        self.submit.setGeometry(45,150,50,25)
        self.cancel = QPushButton("Exit", self)
        self.cancel.setGeometry(105,150,50,25)
        self.submit.setStyleSheet("QPushButton {background-color: #902a39; color: white}")
        self.cancel.setStyleSheet("QPushButton {background-color: #902a39; color: white}")
        self.submit.clicked.connect(self.clickSubmit)
        self.cancel.clicked.connect(self.close)

    def clickSubmit(self):
        date = self.dateedit.date()
        self.start_date = date.dayOfWeek() - 1
        self.week_number.append(" ")
        self.calculate_week_number()
        print(self.start_date)
        print(self.week_number)
        self.close()

    def calculate_week_number(self):
        months = {1: "Jan", 2: "Feb",3: "Mar" ,4:"Apr",5: "May", 6: "Jun", 7: "Jul", 8: "Aug", 9: "Sep", 10: "Oct", 11: "Nov", 12: "Dec"}
        date = self.dateedit.date()
        date = date.addDays(-date.dayOfWeek())
        for week in range(1, 15):
            week_start = date.day()
            week_end = date.addDays(6)
            if week_start < week_end.day():
                string = f"{week} ({months[date.month()]} {week_start}-{week_end.day()})"
            else:
                string = f"{week} ({months[date.month()]} {week_start}-{months[week_end.month()]} {week_end.day()})"
            self.week_number.append(string)
            date = date.addDays(7)

def block_days(room_list, start_day):
    print(start_day)
    for day in range(start_day):
        for room in room_list:
            for hour in range(len(room.schedule[0][day])):
                room.schedule[0][day][hour] = "No Classes"


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = Start_Date()
    w.show()
    sys.exit(app.exec_())
