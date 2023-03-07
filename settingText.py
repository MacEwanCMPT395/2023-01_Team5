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
    

if __name__ == "__main__":
    #first schedule builder window
    App = QApplication(sys.argv)
    window = webapp.MainWindow()
    #start the event loop
    App.exec()

    #making cohorts
    make_cohort(window.listText)

    #print(cohorts.keys()) #printing out cohorts made
    #print(cohorts.values())
    
    #making list of cohorts
    cohort_list = []
    for cohort in cohorts.values(): 
        cohort_list.append(cohort)
    print("cohort list",cohort_list)

    #list of rooms
    print ("rooms list", ROOMS)

    r = algorithm(cohort_list, [Computer_Lab, Room_8])
    print(r)



    '''
    #second schedule builder window
    App2 = QApplication(sys.argv)
    window = scheduleGUI.MainWindow2()
    #start the event loop
    App2.exec()
    print("hello")
    '''

