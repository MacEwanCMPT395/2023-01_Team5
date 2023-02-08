#test data
students = ["Ishan", "Calvin", "Nhi", "Ayesha", "Matt", "Kadia", "Travis", "Aman", "Abeil", "Dariuz",
            "Jon", "Hanibal", "Chad", "Alex", "Jake", "Jordan", "Ginger", "Danielle", "Kelsey", 
            "Keianna", "June", "Chelsea", "Cameron", "Jalen", "Luke", "josh", "Anissa"]

classSize = {24:3, 30:3, 36:2, 40:1}

cohorts = {}

#input functions
def getNumStudents():

    num = int(input("How many students in this core: "))

    return num

def getSpecific():

    specific = input("What specific course does this cohort belong to(use 2 letter abbrev.): ")

    return specific

def getCore():

    core = input("Are these students in PCOM or BCOM: ")

    return core

def getName():

    name = input("Enter name of the cohort starting with 2 letter abbreviation for specific course followed by term(1) and cohort for specific program(1+)(eg. BK11): ")

    return name


#Cohort class + methods
class cohort():

    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.coreProgram = None
        self.specificProgram = None
        self.term = 1
        self.students = []
    

    def __str__(self):
        return self.size

    def __repr__(self):
        return self.name
    

    def __len__(self):
        return self.size

    #def __del__(self):
    #    print(f"Deleted {self.name}\n")

    def setCourses(self, core, specfifc):
        self.coreProgram = core
        self.specificProgram = specific

    def advanceTerm(self):
        self.term += 1

    def addStudent(self, student):
        if len(self.students) == self.size:
            print("Sorry No more room")
        else:
            self.students.append(student)

    def addStudents(self, students):
        if len(students) > self.size:
            print("Sorry not enough space")
        else:
            cohortstudents = students[:self.size]
            self.students = self.students + cohortstudents


def createCohort(name, size, cohorts):
    value = cohort(name, size)
    cohorts[name] = value

#wait to integrate Nhi's algorithm here
'''4
def numCohorts(num):

    #Purpose:
    #Parameters:
    #Return:
    if num > 40:
        temp = 0
        numcohort = 0
        temp = num - 40
        numcohort += 1 
        while temp > 0:
            if temp > 30:
                temp = temp - 36
                classSize[36] -= 1
                numcohort += 1
                print(f"class with capcity of 36 has been used {classSize[36]} remaining")
            elif 24 < temp <= 30:
                temp = temp - 30
                classSize[30] -= 1
                numcohort += 1
                print(f"class with capcity of 30 has been used {classSize[30]} remaining")

            elif 0 < temp <= 24:
                temp = temp - 24
                classSize[24] -= 1
                numcohort += 1
                print(f"class with capcity of 24 has been used {classSize[24]} remaining")
        return numcohort

    elif 36 < num <= 40:
        classSize[40] -= 1
        print("request another room, room 11-458 has been filled")
        return 1

    elif 30 < num <= 36:
        classSize[36] -= 1
        print(f"class with capcity of 36 has been used {classSize[36]} remaining")
        return 1

    elif 24 < num <= 30:
        classSize[30] -= 1
        print(f"class with capcity of 30 has been used {classSize[30]} remaining")
        return 1

    elif 0 < num <= 24:
        classSize[24] -= 1
        print(f"class with capcity of 24 has been used {classSize[24]} remaining")
        return 1

    else:
        print("You input 0 or below")
'''





if __name__ == '__main__':
    '''
    purpose: demo
    '''
    cohortsDict ={}

    students = ["Ishan", "Calvin", "Nhi", "Ayesha", "Matt", "Kadia", "Travis", "Aman", "Abeil", "Dariuz",
            "Jon", "Hanibal", "Chad", "Alex", "Jake", "Jordan", "Ginger", "Danielle", "Kelsey", 
            "Keianna", "June", "Chelsea", "Cameron", "Jalen", "Luke", "josh", "Anissa"]

    size = getNumStudents()

    specific = getSpecific()

    core = getCore()

    name = getName()

    createCohort(name, size, cohortsDict)

    print(cohortsDict)

    createCohort('BK11', 27, cohortsDict)

    print(cohortsDict)

    print(cohortsDict['BK11'].size)

    print(len(students))

    cohortsDict['BK11'].addStudents(students)

    print(cohortsDict['BK11'].students)

    cohortsDict['BK11'].addStudent('Nozick Soleimon')

    print(cohortsDict['BK11'].students)

    cohortsDict['BK11'].setCourses(core, specific)

    print(cohortsDict['BK11'].coreProgram)

    print(cohortsDict['BK11'].specificProgram)

