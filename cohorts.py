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


import math
import numpy as np

students = ["Ishan", "Calvin", "Nhi", "Ayesha", "Matt", "Kadia", "Travis", "Aman", "Abeil", "Dariuz",
            "Jon", "Hanibal", "Chad", "Alex", "Jake", "Jordan", "Ginger", "Danielle", "Kelsey", 
            "Keianna", "June", "Chelsea", "Cameron", "Jalen", "Luke", "josh", "Anissa"]

# We have 9 classrooms
classroom = {"11-533": {'capacity': 36, 'occupied': 'N'}, "11-534": {'capacity': 36, 'occupied': 'N'},\
        "11-560": {'capacity': 24, 'occupied': 'N'}, "11-562": {'capacity': 24, 'occupied': 'N'},\
        "11-564": {'capacity': 24, 'occupied': 'N'}, "11-458": {'capacity': 40, 'occupied': 'N'},\
        "11-430": {'capacity': 30, 'occupied': 'N'}, "11-320": {'capacity': 30, 'occupied': 'N'},\
        "11-532": {'capacity': 30, 'occupied': 'N'}}

term1 = {"BA": 31, "PM" : 24, "GL" : 12, "FS" : 8}
term2 = {"BA": 63, "PM" : 73, "GL" : 18, "FS" : 13}
term3 = {"BA": 74, "PM" : 102, "GL" : 41, "FS" : 18}

data = [term1, term2, term3]

def numCohorts(total):
    '''
    Purpose: 
    Pararmeter: int total num of students enrolled in the program
    return: number of cohorts for specific program

    Condition:
        1. if number of students for each program is <= 20, 
        then we don't split into cohorts

    '''
    if total <= 20:  
        return 1
    
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


def distributeStudents(students, studentsPerCohort, cohorts):
    '''
    Purpose:
    Parameters:
    Return:
    '''
    distributed = {}
    j = 0

    for i in range(cohorts):
        distributed[i] = students[j:(j+studentsPerCohort)]
        j += studentsPerCohort
    return distributed

for i in range (len(data)):
    for k in data[i]:
        cohorts = numCohorts(data[i][k])
        listCohorts = studentsPerCohort(data[i][k], cohorts)
        print(f'program {k} has {data[i][k]} students, divide into {cohorts} cohorts. {listCohorts}')

#print(studentsDistributed)

