'''
STORIES:
1. As a Program Manager, I want to create the right numbers of cohorts, so I can evenly distribute the students in 
each of our seven programs
2. As a Scheduler, I would like to have cohorts clearly matched with their classrooms for all the lectures, so I can 
properly book the rooms.
3, As a Program Manager, I want the cohorts to use the proper naming convention, so I can easily identify them
for our seven programs (e.g., PM0101, PM0102, PM0201, DXD0302).

Want to give some extra space when schedule the cohort 
'''

'''
COHORT requirements:
    - Each student will belong to 2 cohorts
        1. PCOM or BCOM cohort. 
        2. their specific program courses. 

    - PCOM/BCOM on Tue + Thu and the minimum capacity of each class is 30 students
    
'''
import numpy as np

# We have 9 classrooms
classroom = {"11-533": {'capacity': 36, 'occupied': 'N'}, "11-534": {'capacity': 36, 'occupied': 'N'},\
        "11-560": {'capacity': 24, 'occupied': 'N'}, "11-562": {'capacity': 24, 'occupied': 'N'},\
        "11-564": {'capacity': 24, 'occupied': 'N'}, "11-458": {'capacity': 40, 'occupied': 'N'},\
        "11-430": {'capacity': 30, 'occupied': 'N'}, "11-320": {'capacity': 30, 'occupied': 'N'},\
        "11-532": {'capacity': 30, 'occupied': 'N'}}

# 3 terms of students in their Specific program
term1specific = {"BA": 31, "PM" : 24, "GL" : 12, "FS" : 8}
term2specific = {"BA": 63, "PM" : 73, "GL" : 18, "FS" : 13}
term3specific = {"BA": 74, "PM" : 102, "GL" : 41, "FS" : 18}

data = [term1specific, term2specific, term3specific]

# Core Course list of BCOM and PCOM 
term1core = {"PCOM": 64, "BCOM" : 11}
term2core = {"PCOM": 150, "BCOM" : 50}
term3core = {"PCOM": 315, "BCOM" : 35}
dataPBCOM = [term1core, term2core, term3core]

sizeClassroom = [24, 30, 36, 40]  #size of classrooms we have 
#mock class for cohort to test
class Cohort:
    def __init__(self, program, term, cohort, size):
        self.program = program
        self.term = term
        self.cohort = cohort
        self.size = size
    
    def __str__(self):
        return f'{self.program}0{self.term}0{self.cohort}'

# Divide the Cohort 
    '''
    ALgorithm: To populate all of the cohort the size of the room 
    ex: Given the sizes of available classrooms. 
    sizes = [24, 30, 36, 40]

    PCOM size of 150 students will consist of 
            3  * 40-students room with full 40 students = 120
            1  * 30-students room with full 30 students = 30

    In case of the size is 152 students, to prevent a cohort of size (2), 
    we will resize the cohort to 
            3  * 40-students room with full 40 students = 120
            1  * 30-students room with full 30 students = 30
    '''
# def getListOfClassroomSizes(size):
#     print(set(size))
#     return set(size)

def coreCourseCohorts(size, dataPBCOM):
    return 


    
def numCohorts(total):
    '''
    Purpose: 
    Pararmeter: int total num of students enrolled in the program
    return: number of cohorts for specific program

    Condition:
        1. if number of students for each program is <= 20, 
        then we don't split into cohorts

    '''
    # 1 cohort case 
    if total <= 20:  
        return 1
    
    # start with 2 cohorts
    n = 2
    while (total // n) > 30: 
        n += 1
    return n

def studentsPerCohort(total, n):
    '''
    Purpose:
    Parameters:
    Return:
    '''
    listCohort = []
    studentsInCohort = total // n

    for i in range (n-1):
        listCohort.append(studentsInCohort) 

    #The last case
    if (total % n != 0): #if it is not evenly distributed
        listCohort.append(studentsInCohort + (total % n))
    else: 
        listCohort.append(studentsInCohort) 
    return listCohort

def createCohortObj(program, term, cohort, size):
    cohort = Cohort (program, term, cohort, size)
    return cohort


def main():
    for term in range (len(data)):
        for program in data[term]:
            cohorts = numCohorts(data[term][program])
            listCohorts = studentsPerCohort(data[term][program], cohorts)
            print(f'program {program} has {data[term][program]} students, divide into {cohorts} cohorts.')
            for c in range (len(listCohorts)):
                cohort = createCohortObj(program, term, c+1, listCohorts[c])
                print(cohort)

main()
