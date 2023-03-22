from data_structures import *

'''
Function Name: addCourse

Purpose: add course to our list of courses for the appropriate program and term

Parameters: 
        program: Which program(abbrev.) does course belong to (eg. PCOM(string)) 

        course: What course and number to be added separated by an underscore
                (Eg. CMSK_0101(String))
        term: Which term will this course be taken (Eg. 1, 2, or 3(Int))
        hours: How many hours will it take to complete the course (Eg. 34 (Int))
        lab: is there a lab component for the lab (Eg. yes or no (string)(will be 
             converted into a boolean))

Example:
        addCourse(PCOM, CMSK_0101, 1, 34, no)

        Result:
            CMSK_0101 (course object will be created)
            if course doesnt exist it will be added to the array of courses for 
            that program and term

            PCOMT1 = [..., ..., "CMSK_0101"]
            PCOM_TERM_1 = [..., ..., CMSK_0101]


'''

def addCourse(program, course, term, hours, lab):

    #initialize variables
    program = program.upper()
    course  = course.upper()
    term = int(term)
    exist = False
    lab = lab.upper()

    if lab == "YES":
        lab = True
    else:
        lab = False
    

    #check if course already exists
    if program == "PCOM":
        if term == 1:
            if course in PCOMT1:
                exist = True
        elif term == 2:
            if course in PCOMT2:
                exist = True
        elif term == 3:
            if course in PCOMT3:
                exist = True
    elif program == "BCOM":
        if term == 1:
            if course in BCOMT1:
                exist = True
        elif term == 2:
            if course in BCOMT2:
                exist = True
        elif term == 3:
            if course in BCOMT3:
                exist = True
    elif program == "FS":
        if term == 1:
            if course in FST1:
                exist = True
        elif term == 2:
            if course in FST2:
                exist = True
        elif term == 3:
            if course in FST3:
                exist = True
    elif program == "DXDI":
        if term == 1:
            if course in DXDIT1:
                exist = True
        elif term == 2:
            if course in DXDIT2:
                exist = True
        elif term == 3:
            if course in DXDIT3:
                exist = True
    elif program == "BK":
        if term == 1:
            if course in BKT1:
                exist = True
        elif term == 2:
            if course in BKT2:
                exist = True
        elif term == 3:
            if course in BKT3:
                exist = True
    elif program == "GLM":
        if term == 1:
            if course in GLT1:
                exist = True
        elif term == 2:
            if course in GLT2:
                exist = True
        elif term == 3:
            if course in GLT3:
                exist = True
    elif program == "BA":
        if term == 1:
            if course in BAT1:
                exist = True
        elif term == 2:
            if course in BAT2:
                exist = True
        elif term == 3:
            if course in BAT3:
                exist = True
    elif program == "PM":
        if term == 1:
            if course in PMT1:
                exist = True
        elif term == 2:
            if course in PMT2:
                exist = True
        elif term == 3:
            if course in PMT3:
                exist = True

    return lab

    #if it doesnt exist
        #append to ref list
        #create course object
        #append to list of course objects

def main():
    a = addCourse("pm","pcom_0131", 3, 18, "no")
    print(a)


main()