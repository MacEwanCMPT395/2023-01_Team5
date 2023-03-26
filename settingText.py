import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import webapp
from data_structures import *
from algorithm import *
from cohorts import *
from request_rooms import *
import scheduleGUI


# dictionary to hold cohorts
program_names = ["PM1", "PM2", "PM3", "BA1", "BA2", "BA3", "GLM1", "GLM2", "GLM3", "FS1", "FS2", "FS3", "DXD1", "DXD2", "DXD3", "BK1", "BK2", "BK3", "PCOM1", "PCOM2", "PCOM3", "BCOM1", "BCOM2", "BCOM3"] #used for naming
cohorts = {} #store Cohort objects

def make_cohort(list12):
    program_size = list12
    program_num = 0 # used to index program_size array
    for num_registrants in program_size:
        num_cohorts = numCohorts(num_registrants)
        listCohorts = studentsPerCohort(num_registrants, num_cohorts)
        cohort_num = 1 # used to name cohort and input cohort number in cohort object
        for num in listCohorts:
            if num == 0:
                continue
            name = f'{program_names[program_num]}{cohort_num}'
            cohorts[name] = Cohort(name, num, cohort_num)
            cohort_num += 1
        program_num += 1


def make_room_object(room_list_raw, room_list):
    for room in room_list_raw:
        if room[1] == "Y":
            room.append(Room(room[0], room[2], True))
        else:
            room_list.append(Room(room[0], room[2], False))


def restart():
    QtCore.QCoreApplication.quit()
    
    status = QtCore.QProcess.startDetached(sys.executable, sys.argv) 
    print (status)


def main():
    #first schedule builder window
    App = QApplication(sys.argv)
    window = webapp.MainWindow()
    #start the event loop
    App.exec()

    #making room list
    globalRoomList = []
    print(globalRoomList)

    #making cohorts
    make_cohort(window.listText)

    #print(cohorts.keys()) #printing out cohorts made
    #print(cohorts.values())
    
    #making list of cohorts
    cohort_list = []
    for cohort in cohorts.values():
        cohort_list.append(cohort)

    listOfRooms = algorithm(cohort_list, [Computer_Lab, Room_8])

    #second schedule builder window
    App2 = QApplication(sys.argv)
    window2 = scheduleGUI.MainWindow2(listOfRooms)
    #start the event loop
    App2.exec()

    window2.redo.clicked.connect(restart())

    print("hello")


if __name__ == "__main__":
    main()
    

