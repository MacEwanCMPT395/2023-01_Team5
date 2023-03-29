from data_structures import *


#globals
lecture_hours_program = {"PM1": 56, "PM2": 70, "PM3": 53, "BA1": 70, "BA2": 70, "BA3":53, "GLM1": 57, "GLM2": 36, "GLM3": 60,
    "DXD3": 36, "BK1": 42, "BK2": 12}

lecture_hours_core = {"PCOM1": 70, "PCOM2": 70, "PCOM3": 74, "BCOM1": 71, "BCOM2": 63, "BCOM3": 70}

lab_hours_program = {"FS1": 80, "FS2": 86, "FS3": 50, "DXD1": 66, "DXD2":84, "DXD3": 45, "BK2": 56, "BK3": 54}

lab_hours_core = {"PCOM1": 31, "PCOM2": 18, "PCOM3": 8}


unscehduled_cohorts = []
#need to add case for FS night classes
def request_room(cohorts, room_list):
    total_room_hours = WEEKS * 18
    total_room_hours_night = WEEKS * 16

    rooms_program = []
    rooms_core = []
    labs = []
    hours_remaining_program = {}
    hours_remaining_core = {}
    hours_remaining_night = {}

    #make room list
    for room in room_list:
        if not room.is_lab:
            rooms_program.append(room)
            rooms_core.append(room)
        else:
            rooms_program.append(room)
            rooms_core.append(room)
            labs.append(room)

    for room in rooms_program:
        hours_remaining_program[str(room)] = total_room_hours
        hours_remaining_core[str(room)] =  total_room_hours

    for lab in labs:
        hours_remaining_night[str(lab)] = total_room_hours_night

    rooms_program.sort(key=lambda room: room.capacity)
    rooms_core.sort(key=lambda room: room.capacity)

    #loop through every cohort
    for cohort in cohorts.values():
        #check if it is a program specific with lecture
        if cohort.name[:len(cohort.name) - 1] in lecture_hours_program.keys():
            scheduled = False
            for room in rooms_program:
                #determine classroom assigned to each cohort and check if the classroom has enough hours remaining to hold cohort
                if cohort.size <= room.capacity and hours_remaining_program[room.room_number] >= lecture_hours_program[cohort.name[:len(cohort.name) - 1]] and not room.is_lab:
                    #if it does, reduce the hours in the classroom
                    hours_remaining_program[room.room_number] -= lecture_hours_program[cohort.name[:len(cohort.name) - 1]]
                    scheduled = True
                    break
            if not scheduled:
                unscehduled_cohorts.append("Lecture")

        #check if it is a program specific with lab
        if cohort.name[:len(cohort.name) - 1] in lab_hours_program.keys():
            scheduled = False
            #separate case for FS
            if cohort.name[:len(cohort.name) - 2] == "FS":
                for room in labs:
                    if hours_remaining_night[room.room_number] >= lab_hours_program[cohort.name[:len(cohort.name) - 1]] and cohort.size <= room.capacity:
                        #if it does, reduce the hours in the classroom
                        hours_remaining_night[room.room_number] -= lab_hours_program[cohort.name[:len(cohort.name) - 1]]
                        scheduled = True
                        break
            else:
                for room in labs:
                    if hours_remaining_program[room.room_number] >= lab_hours_program[cohort.name[:len(cohort.name) - 1]] and cohort.size <= room.capacity:
                        #if it does, reduce the hours in the classroom
                        hours_remaining_program[room.room_number] -= lab_hours_program[cohort.name[:len(cohort.name) - 1]]
                        scheduled = True
                        break
            if not scheduled and cohort.name[:len(cohort.name) - 2] == "FS":
                unscehduled_cohorts.append("Evening Computer Lab")
            elif not scheduled:
                unscehduled_cohorts.append("Daytime Computer Lab")
        #check if it is core with lecture
        if cohort.name[:(len(cohort.name) - 1)] in lecture_hours_core.keys():
            scheduled = False
            for room in rooms_core:
                #determine classroom assigned to each cohort and check if the classroom has enough hours remaining to hold cohort
                if cohort.size <= room.capacity and hours_remaining_core[room.room_number] >= lecture_hours_core[cohort.name[:len(cohort.name) - 1]] and not room.is_lab:
                    #if it does, reduce the hours in the classroom
                    hours_remaining_core[room.room_number] -= lecture_hours_core[cohort.name[:len(cohort.name) - 1]]
                    scheduled = True
                    break
            if not scheduled:
                unscehduled_cohorts.append("Lecture")

        #check if it is core with lab
        if cohort.name[:len(cohort.name) - 1] in lab_hours_core.keys():
            scheduled = False
            for room in labs:
                if hours_remaining_core[room.room_number] >= lab_hours_core[cohort.name[:len(cohort.name) - 1]] and cohort.size <= room.capacity:
                    #if it does, reduce the hours in the classroom
                    hours_remaining_core[room.room_number] -= lab_hours_core[cohort.name[:len(cohort.name) - 1]]
                    scheduled = True
            if not scheduled:
                unscehduled_cohorts.append("Daytime Computer Lab")
    #check if all cohorts scheduled
    #print("Core course:" + str(hours_remaining_core.items()))
    #print("Program specific:" + str(hours_remaining_program.items()))
    #print("Night lab:" + str(hours_remaining_night.items()))
    return set(unscehduled_cohorts)

def create_room(course, room_size, room_list):
    if course.requireslab == True:
        new_room = Room("Extra lab", room_size, True)
    else:
        new_room = Room("Extra lecture", room_size, False)
    room_list.append(new_room)
