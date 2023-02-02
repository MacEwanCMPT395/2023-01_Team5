import math
import numpy as np


students = ["Ishan", "Calvin", "Nhi", "Ayesha", "Matt", "Kadia", "Travis", "Aman", "Abeil", "Dariuz",
            "Jon", "Hanibal", "Chad", "Alex", "Jake", "Jordan", "Ginger", "Danielle", "Kelsey", 
            "Keianna", "June", "Chelsea", "Cameron", "Jalen", "Luke", "josh", "Anissa"]



def cohortsCalc(num=0):
    '''
    Purpose: 
    Pararmeter: int (represents how many students enrolled in that program)
    return: minimum number of cohorts to accomodate registered students
    '''
    minCohorts = math.ceil(num // 24)

    if (num - minCohorts != 0):
        minCohorts += 1

    return minCohorts

def studentsPerCohort(students, cohorts):
    '''
    Purpose:
    Parameters:
    Return:
    '''

    studentsInCohort = students // cohorts

    if students - (studentsInCohort * cohorts) != 0:
        print(f"students remaining: ", students - (studentsInCohort * cohorts))

    return studentsInCohort


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

    #remainder = len(students) - 
    return distributed
    '''
    distributed = []
    cohort = []

    start = 0
    i = 0

    while i < len(students):
        for student in students:
            if i < studentsPerCohort:
                cohort.append(student)
                i+=1
            elif i == studentsPerCohort:
                distributed.append(cohort)
                cohort.clear()
        

    return distributed
    '''



    
#for index, student in enumerate(studentsDistributed):
    #print(index, student)

    #return np.array_split(students, studentsPerCohort)



cohorts = cohortsCalc(len(students))

studentsInCohort = studentsPerCohort(len(students), cohorts)

studentsDistributed = distributeStudents(students, studentsInCohort, cohorts)

print(len(students))
print(cohorts)
print(studentsInCohort)
print(studentsDistributed)
