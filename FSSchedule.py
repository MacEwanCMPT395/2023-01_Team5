import datetime

from tabulate import tabulate
from datetime import datetime, timedelta

#Data of courses in appropriate order
FS1 = [["CMSK0150", 28], ["CMSK0151", 28], ["CMSK0152", 28], ["CMSK0157", 28], ["CMSK0154", 28]]
FS2 = [["CMSK0153", 35], ["CMSK0200", 28], ["CMSK0201", 35], ["CMSK0203", 28], ["CMSK0202", 35]]
FS3 = [["PCOM0160", 91]]
DXD1 = [["AVDM0165", 21], ["DXDI0101", 28], ["DXD", 28]]
DXD2 = [["AVDM0170", 21], ["AVDM0138", 21], ["DXDI0103", 28], ["DXDI0104", 28]]
DXD2 = [["AVDM0238", 14], ["AVDM0270", 49], ["DXDI9901", 56]]
Time1 = ["4:30-5:00", "5:00-5:30", "5:30-6:00", "6:00-6:30", "6:30-7:00", "7:00-7:30", "7:30-8:00",
         "8:00-8:30"]
Time2 = ["8:00-8:30", "8:30-9:00", "9:00-9:30", "9:30-10:00", "10:00-10:30", "10:30-11:00"]
Room = "11-532 Computer Lab"





#FUNCTION TO CREATE A SCHEDULE
def makeFSScheduleT1():
    date = input("What date does term start(eg. July 26, 2023): ")
    startDate = datetime.strptime(date, '%B %d, %Y')
    course = []
    dates = []

    #Fills course list

    time = Time1
    for i in range(len(Time1)):
        if i < 4:
            course.append(FS1[0][0])
        else:
            course.append(FS1[1][0])

    #Fill the dates list
    tdelta = timedelta(days=FS1[0][1])
    endDate = startDate + tdelta
    for i in range(len(time)):
        dates.append(f"{startDate.date()} - {endDate.date()}")

    #create first part of term in a schedule dictionary and print
    schedule1 = {'Time': time, 'Course': course, 'Dates':dates}
    print(Room)
    print("Tuesday & Thursday")
    print(tabulate(schedule1, headers="keys", tablefmt="fancy_grid"))


    #start second set of courses
    course.clear()
    dates.clear()
    for i in range(len(Time1)):
        if i < 4:
            course.append(FS1[2][0])
    #set next range of dates
    startDate = endDate
    tdelta = timedelta(days=FS1[2][1])
    endDate = startDate + tdelta
    for i in range(len(time)-4):
        dates.append(f"{startDate.date()} - {endDate.date()}")

    #Create and print second part of schedule
    schedule2 = {'Time': time, 'Course': course, 'Dates':dates}
    print(Room)
    print("Tuesday & Thursday")
    print(tabulate(schedule2, headers="keys", tablefmt="fancy_grid"))

    #start last part of term1 schedule
    course.clear()
    dates.clear()
    for i in range(len(Time1)):
        if i < 4:
            course.append(FS1[3][0])
        else:
            course.append(FS1[4][0])
    # set next range of dates
    startDate = endDate
    tdelta = timedelta(days=FS1[3][1])
    endDate = startDate + tdelta
    for i in range(len(time)):
        dates.append(f"{startDate.date()} - {endDate.date()}")

    # Create and print third part of schedule
    schedule3 = {'Time': time, 'Course': course, 'Dates': dates}
    print(Room)
    print("Tuesday & Thursday")
    print(tabulate(schedule3, headers="keys", tablefmt="fancy_grid"))

def makeFSScheduleT2():
    date = input("What date does term start(eg. July 26, 2023): ")
    startDate = datetime.strptime(date, '%B %d, %Y')
    course = []
    dates = []

    #Fills course list

    time = Time1
    for i in range(len(Time1)):
        if i < 4:
            course.append(FS2[0][0])
        else:
            course.append(FS2[1][0])

    #Fill the dates list
    tdelta = timedelta(days=FS2[0][1])
    endDate = startDate + tdelta
    for i in range(len(time)):
        dates.append(f"{startDate.date()} - {endDate.date()}")

    #create first part of term in a schedule dictionary and print
    schedule1 = {'Time': time, 'Course': course, 'Dates':dates}
    print(Room)
    print("Tuesday & Thursday")
    print(tabulate(schedule1, headers="keys", tablefmt="fancy_grid"))


    #start second set of courses
    course.clear()
    dates.clear()
    for i in range(len(Time1)):
        if i < 4:
            course.append(FS2[2][0])
    #set next range of dates
    startDate = endDate
    tdelta = timedelta(days=FS1[2][1])
    endDate = startDate + tdelta
    for i in range(len(time)-4):
        dates.append(f"{startDate.date()} - {endDate.date()}")

    #Create and print second part of schedule
    schedule2 = {'Time': time, 'Course': course, 'Dates':dates}
    print(Room)
    print("Tuesday & Thursday")
    print(tabulate(schedule2, headers="keys", tablefmt="fancy_grid"))

    #start last part of term1 schedule
    course.clear()
    dates.clear()
    for i in range(len(Time1)):
        if i < 4:
            course.append(FS2[3][0])
        else:
            course.append(FS2[4][0])
    # set next range of dates
    startDate = endDate
    tdelta = timedelta(days=FS2[3][1])
    endDate = startDate + tdelta
    for i in range(len(time)):
        dates.append(f"{startDate.date()} - {endDate.date()}")

    # Create and print third part of schedule
    schedule3= {'Time': time, 'Course': course, 'Dates': dates}
    print(Room)
    print("Tuesday & Thursday")
    print(tabulate(schedule3, headers="keys", tablefmt="fancy_grid"))

def makeFSScheduleT3():
    date = input("What date does term start(eg. July 26, 2023): ")
    startDate = datetime.strptime(date, '%B %d, %Y')
    course = []
    dates = []

    # Fills course list
    time = Time1
    for i in range(len(Time1)):
        if i < 4:
            course.append(FS3[0][0])


    # Fill the dates list
    tdelta = timedelta(days=FS3[0][1])
    endDate = startDate + tdelta
    for i in range(len(time)):
        dates.append(f"{startDate.date()} - {endDate.date()}")

    # create first part of term in a schedule dictionary and print
    schedule1 = {'Time': time, 'Course': course, 'Dates': dates}
    print(Room)
    print("Monday & Wednesday")
    print(tabulate(schedule1, headers="keys", tablefmt="fancy_grid"))
    #if program == "FS":






def main():
    program = input("What specific program FS: ")
    term = int(input("What term: "))
    if program.upper() == "FS" and term == 1:
        makeFSScheduleT1()
    elif program.upper() == "FS" and term == 2:
        makeFSScheduleT2()
    elif program.upper() == "FS" and term == 3:
        makeFSScheduleT3()
    else:
        print("")

main()