import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import webapp
from data_structures import *
from algorithm import *
from cohorts import *


# Mock cohort splitting algo to test
def test_data(program_size):
    if program_size == 0:
        return
    res = []
    num = program_size
    for _ in range(1):
        res.append(num)
    res[0] += program_size
    return res

'''#mock class for cohort to test
class Cohort:
    def __init__(self, name, num, size) -> None:
        self.name = name
        self.num = num
        self.size = size'''

'''
CODE STARTS HERE
'''
# dictionary to hold cohorts
program_names = ["PM1", "PM2", "PM3", "BA1", "BA2", "BA3", "GLM1", "GLM2", "GLM3", "FS1", "FS2", "FS3", "DXD1", "DXD2", "DXD3", "BK1", "BK2", "BK3", "PCOM1", "PCOM2", "PCOM3", "BCOM1", "BCOM2", "BCOM3"] #used for naming
cohorts = {} #store Cohort objects

def make_cohort(list12):
    program_size = list12
    program_num = 0 # used to index program_size array
    for num_registrants in program_size:
        #insert cohort dividing algorithm here instead
            #return dictionary
        '''Test code (delete after)'''
        num_cohorts = numCohorts(num_registrants)
        listCohorts = studentsPerCohort(num_registrants, num_cohorts)
        ''''''''''''
        cohort_num = 1 # used to name cohort and input cohort number in cohort object
        for num in listCohorts:
            if num == 0:
                continue
            name = f'{program_names[program_num]}{cohort_num}'
            cohorts[name] = Cohort(name, num, cohort_num)
            cohort_num += 1
        program_num += 1

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = webapp.MainWindow()
    #start the event loop
    App.exec()
    make_cohort(window.listText)
    #test(cohorts)
    
    '''for i in cohorts.keys():
        print(f' {cohorts[i].name} {cohorts[i].size}')'''
    #print('hello')
    