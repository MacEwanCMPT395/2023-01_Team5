from data_structures import *

'''
Function Name: addCourse

Purpose: add course to our list of courses for the appropriate program and term

Parameters: 
        list: Which program(abbrev.) does course belong to (eg. PCOM(string)) 
        valid lists: PCOM_TERM_1, PCOM_TERM_2, PCOM_TERM_3, BCOM_TERM_1, BCOM_TERM_2,
                     BCOM_TERM_3, FS_TERM_1, FS_TERM_2, FS_TERM_3, DXDI_TERM_1, DXDI_TERM_2
                     DXDI_TERM_3, BK_TERM_1, BK_TERM_2, BK_TERM_3, GL_TERM_1, GL_TERM_2, 
                     GL_TERM_3, BA_TERM_1, BA_TERM_2, BA_TERM_3, PM_TERM_1, PM_TERM_2
                     PM_TERM_3. 

        course_name: What course and number to be added separated by an underscore
                     (Eg. CMSK_0101(String))
 
        hours: How many hours will it take to complete the course (Eg. 34 (Int))

        lab: is there a lab component for the lab (Eg. yes or no (string)(will be 
             converted into a boolean))
            
        hourPerDay: (string that will be converted to an int) represents how long the lecture 
                    runs per day 
                    options: "90 minutes" (converts to 1), "120 minutes" (converts to 2)
                             "180 minutes" (converts to 3)

Example:
        addCourse(PCOM_TERM_1, "CMSK_0101", 34, "no")

        Result:
            CMSK_0101 (course object will be created)
            if course doesnt exist it will be added to the array of courses for 
            that program and term

            before function call:
                PCOM_TERM_1 = [..., ...]
            after:
                PCOM_TERM_1 = [..., ..., CMSK_0101]


'''
def addCourse(list, course_name, hours, lab, hoursPerDay):
    #initialize variables
    course  = course_name.upper()
    hours = int(hours)
    exist = False
    lab = lab.upper()
    
    #set slot_type variable for our course class object
    if hoursPerDay == "90 minutes":
        hoursPerDay = 1
    elif hoursPerDay == "120 minutes":
        hoursPerDay = 2
    elif hoursPerDay == "180 minutes":
        hoursPerDay = 3

    #set appropriate list to check
    if list == "PCOM_TERM_1":
         list = PCOM_TERM_1
    elif list == "PCOM_TERM_2":
        list = PCOM_TERM_2
    elif list == "PCOM_TERM_3":
        list = PCOM_TERM_3
    elif list =="BCOM_TERM_1":
        list = BCOM_TERM_1 
    elif list =="BCOM_TERM_2":
        list = BCOM_TERM_2
    elif list == "BCOM_TERM_3":
        list = BCOM_TERM_3
    elif list == "FS_TERM_1":
        list = FS_TERM_1
    elif list == "FS_TERM_2":
        list = FS_TERM_2
    elif list == "FS_TERM_3":
        list = FS_TERM_3
    elif list == "DXDI_TERM_1":
        list = DXDI_TERM_1 
    elif list == "DXDI_TERM_2":
        list = DXDI_TERM_2
    elif list == "DXDI_TERM_3":
        list = DXDI_TERM_3
    elif list == "BK_TERM_1":
        list = BK_TERM_1
    elif list == "BK_TERM_2":
        list = BK_TERM_2 
    elif list == "BK_TERM_3":
        list = BK_TERM_3
    elif list == "GL_TERM_1":
        list = GL_TERM_1 
    elif list == "GL_TERM_2":
        list = GL_TERM_2 
    elif list == "GL_TERM_3":
        list = GL_TERM_3
    elif list == "BA_TERM_1":
        list = BA_TERM_1
    elif list == "BA_TERM_2":
        list = BA_TERM_2 
    elif list == "BA_TERM_3":
        list = BA_TERM_3 
    elif list == "PM_TERM_1":
        list = PM_TERM_1
    elif list == "PM_TERM_2":
        list = PM_TERM_2
    elif list == "PM_TERM_3":
        list = PM_TERM_3

    #convert lab requirement to boolean
    if lab == "YES":
        lab = True
    else:
        lab = False
    
    #check if course is in list
    if course in list:
        exist = True
    
    #if course not in list create the object and addit to list
    if exist == False:
        new_course = Course(course, hours, lab, hoursPerDay)
        list.append(new_course)


'''
Function Name: removeCourse

Purpose: removes course from our list of courses for the appropriate program and term

Parameters: 
        list: Which program(abbrev.) does course belong to (eg. PCOM(string)) 
        valid lists: PCOM_TERM_1, PCOM_TERM_2, PCOM_TERM_3, BCOM_TERM_1, BCOM_TERM_2,
                     BCOM_TERM_3, FS_TERM_1, FS_TERM_2, FS_TERM_3, DXDI_TERM_1, DXDI_TERM_2
                     DXDI_TERM_3, BK_TERM_1, BK_TERM_2, BK_TERM_3, GL_TERM_1, GL_TERM_2, 
                     GL_TERM_3, BA_TERM_1, BA_TERM_2, BA_TERM_3, PM_TERM_1, PM_TERM_2
                     PM_TERM_3. 

        course_name: What course and number to be removed separated by an underscore
                (Eg. CMSK_0101(String))
        

Example:
        removeCourse(PCOM, "CMSK_0101")

        Result:
            CMSK_0101 (course object will be created)
            if course doesnt exist it will be added to the array of courses for 
            that program and term

            Before function call:
                PCOM_TERM_1 = [..., ..., CMSK_0101]
            After:
               PCOM_TERM_1 = [..., ...]


'''    
def removeCourse(list, course_name):
    #initialize variables
    course  = course_name.upper()
    exist = False
    i = 0
    index = 0
    #set appropriate list to check
    if list == "PCOM_TERM_1":
         list = PCOM_TERM_1
    elif list == "PCOM_TERM_2":
        list = PCOM_TERM_2
    elif list == "PCOM_TERM_3":
        list = PCOM_TERM_3
    elif list =="BCOM_TERM_1":
        list = BCOM_TERM_1 
    elif list =="BCOM_TERM_2":
        list = BCOM_TERM_2
    elif list == "BCOM_TERM_3":
        list = BCOM_TERM_3
    elif list == "FS_TERM_1":
        list = FS_TERM_1
    elif list == "FS_TERM_2":
        list = FS_TERM_2
    elif list == "FS_TERM_3":
        list = FS_TERM_3
    elif list == "DXDI_TERM_1":
        list = DXDI_TERM_1 
    elif list == "DXDI_TERM_2":
        list = DXDI_TERM_2
    elif list == "DXDI_TERM_3":
        list = DXDI_TERM_3
    elif list == "BK_TERM_1":
        list = BK_TERM_1
    elif list == "BK_TERM_2":
        list = BK_TERM_2 
    elif list == "BK_TERM_3":
        list = BK_TERM_3
    elif list == "GL_TERM_1":
        list = GL_TERM_1 
    elif list == "GL_TERM_2":
        list = GL_TERM_2 
    elif list == "GL_TERM_3":
        list = GL_TERM_3
    elif list == "BA_TERM_1":
        list = BA_TERM_1
    elif list == "BA_TERM_2":
        list = BA_TERM_2 
    elif list == "BA_TERM_3":
        list = BA_TERM_3 
    elif list == "PM_TERM_1":
        list = PM_TERM_1
    elif list == "PM_TERM_2":
        list = PM_TERM_2
    elif list == "PM_TERM_3":
        list = PM_TERM_3
    #check if course exists and grab its index
    for i in range(len(list)):
        if list[i].name == course:
            exist = True
        else:
            index += 1
    
    #if course exists remove it
    if exist == True:
        list.pop(index)

'''
Function Name: editCourse

Purpose: edit an existing courses attributes eg. course name, hours, lab requirement

Parameters: 
        list: Which program(abbrev.) does course belong to (eg. PCOM(string)) 
        valid lists: PCOM_TERM_1, PCOM_TERM_2, PCOM_TERM_3, BCOM_TERM_1, BCOM_TERM_2,
                     BCOM_TERM_3, FS_TERM_1, FS_TERM_2, FS_TERM_3, DXDI_TERM_1, DXDI_TERM_2
                     DXDI_TERM_3, BK_TERM_1, BK_TERM_2, BK_TERM_3, GL_TERM_1, GL_TERM_2, 
                     GL_TERM_3, BA_TERM_1, BA_TERM_2, BA_TERM_3, PM_TERM_1, PM_TERM_2
                     PM_TERM_3.

        oldCourse: What course do you want to0 change (Eg. pcom_0199(String))

        newCourse: New name of the course(Eg. cmsk_0199(string))
      
        hours: How many hours will it take to complete the course (Eg. 34 (Int))
        
        lab: is there a lab component for the lab (Eg. yes or no (string)(will be 
             converted into a boolean))
        
        hourPerDay: (string that will be converted to an int) represents how long the lecture 
                    runs per day 
                    options: "90 minutes" (converts to 1), "120 minutes" (converts to 2)
                             "180 minutes" (converts to 3)

Example:
        editCourse(PCOM_TERM_3, "CMSK_0101", "PCOM_0199", 34, no)

        Result:
            CMSK_0101 (course name will be changed to PCOM_0199)
            if course exist it will change the attributes like so given above example:
            course name will change to PCOM_0199
            hours will change to 34
            lab requirement will change to False
            
            before function call:
                PCOM_TERM_3 = [..., ..., CMSK_0101]
            after function call:
                PCOM_TERM_3 = [..., ..., PCOM_0199]

'''
def editCourse(list, oldCourse, newCourse, hours, lab, hoursPerDay):
    #initialize variables
    oldCourse = oldCourse.upper()
    newCourse = newCourse.upper()
    hours = int(hours)
    lab = lab.upper()
    exist = False
    i = 0
    index = 0

    #set slot_type variable for our course class object
    if hoursPerDay == "90 minutes":
        hoursPerDay = 1
    elif hoursPerDay == "120 minutes":
        hoursPerDay = 2
    elif hoursPerDay == "180 minutes":
        hoursPerDay = 3

    #set appropriate list to check
    if list == "PCOM_TERM_1":
         list = PCOM_TERM_1
    elif list == "PCOM_TERM_2":
        list = PCOM_TERM_2
    elif list == "PCOM_TERM_3":
        list = PCOM_TERM_3
    elif list =="BCOM_TERM_1":
        list = BCOM_TERM_1 
    elif list =="BCOM_TERM_2":
        list = BCOM_TERM_2
    elif list == "BCOM_TERM_3":
        list = BCOM_TERM_3
    elif list == "FS_TERM_1":
        list = FS_TERM_1
    elif list == "FS_TERM_2":
        list = FS_TERM_2
    elif list == "FS_TERM_3":
        list = FS_TERM_3
    elif list == "DXDI_TERM_1":
        list = DXDI_TERM_1 
    elif list == "DXDI_TERM_2":
        list = DXDI_TERM_2
    elif list == "DXDI_TERM_3":
        list = DXDI_TERM_3
    elif list == "BK_TERM_1":
        list = BK_TERM_1
    elif list == "BK_TERM_2":
        list = BK_TERM_2 
    elif list == "BK_TERM_3":
        list = BK_TERM_3
    elif list == "GL_TERM_1":
        list = GL_TERM_1 
    elif list == "GL_TERM_2":
        list = GL_TERM_2 
    elif list == "GL_TERM_3":
        list = GL_TERM_3
    elif list == "BA_TERM_1":
        list = BA_TERM_1
    elif list == "BA_TERM_2":
        list = BA_TERM_2 
    elif list == "BA_TERM_3":
        list = BA_TERM_3 
    elif list == "PM_TERM_1":
        list = PM_TERM_1
    elif list == "PM_TERM_2":
        list = PM_TERM_2
    elif list == "PM_TERM_3":
        list = PM_TERM_3

    #turn lab argument into a boolean
    if lab == "YES":
        lab = True
    else:
        lab = False
    
    #check to see whether old course exists
    for i in range(len(list)):
        if list[i].name == oldCourse:
            exist = True
            index = i
    
    #If old course exists edit the attributes
    if exist == True:
        list[index].name = newCourse
        list[index].hours = hours
        list[index].requires_lab = lab
        list[index].slot_type = hoursPerDay

    
#Test functions

def main():
    addCourse("PCOM_TERM_3","pcom_0131", 18, "no" , "120 minutes")
    print(PCOM_TERM_3)
    print(PCOM_TERM_3[-1].name)
    print(PCOM_TERM_3[-1].hours)
    print(PCOM_TERM_3[-1].requires_lab)
    print(PCOM_TERM_3[-1].slot_type)

    editCourse("PCOM_TERM_3", "pcom_0131", "cmsk_0199", 28, "yes", "180 minutes")

    print(PCOM_TERM_3[-1].name)
    print(PCOM_TERM_3[-1].hours)
    print(PCOM_TERM_3[-1].requires_lab)
    print(PCOM_TERM_3[-1].slot_type)

    removeCourse("PCOM_TERM_3", "pcom_0131")
    print(PCOM_TERM_3)
    removeCourse("PCOM_TERM_3", "cmsk_0199")
    print(PCOM_TERM_3)




main()