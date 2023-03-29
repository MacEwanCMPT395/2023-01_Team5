from data_structures import *


def find_room(all_rooms):
    for room in all_rooms:
        if room.capacity == room.capacity:
            return room
        else:
            continue

def adjust_slot(slot, course):
    if course.slot_type == 1:
        slot += 3
    else:
        slot += course.slot_type * 2
    return slot 

def split_rooms(all_rooms):
    lab_rooms = []

    for room in all_rooms:
        if room.is_lab:
            lab_rooms.append(room)
            all_rooms.remove(room)
    return all_rooms, lab_rooms


def algorithm(cohorts, rooms):
    """
    :param cohorts: List of cohorts.
    :param rooms: List of available rooms.
    """
    # Get our lecture rooms and lab rooms in separate lists.
    lectures, labs = split_rooms(rooms)

    extra_lab_num = 1
    extra_lec_num = 1
    
    for cohort in cohorts:
        slot = 0
        # Goes through each course in each cohort.
        for course in cohort.courses:  # Each course needs to be placed correctly.
            
            # Find correct room type
            available_rooms = lectures
            if course.requires_lab:
                available_rooms = labs


            found = False
            # Find correct room size
            for room in available_rooms:
                week = 0
                # Prevents Course from being schduled multiple times
                if found:
                    break
                
                # Correct Room size found.
                if cohort.room_size <= room.capacity:
                    

                    # Slot reset Condition
                    if room.is_lab and slot > 21:
                        slot = 0
                    else:
                        if slot > 14:
                            slot = 0

                    # Ensuring Correct Weekday.
                    if course in GENERAL:
                        weekday = 0
                    
                    else:
                        weekday = 1
                        
                    # Monday/Wednesday Scanning and Placement
                    while week < WEEKS:
                            
                        # First day scan (Monday/Tuesday)
                        if room.scan(course, week, weekday, slot) and cohort.scan(course, week, weekday, slot):
                                room.update_schedule(course, cohort, week, weekday, slot)
                                cohort.update_schedule(course, room, week, weekday, slot)
                                found = True
                                slot = adjust_slot(slot, course)
                                break
                            
                        # Second day scan (Wedensday/Thursday)
                        if room.scan(course, week, weekday + 2, slot) and cohort.scan(course, week, weekday + 2, slot):
                                room.update_schedule(course, cohort, week, weekday + 2, slot)
                                cohort.update_schedule(course, room, week, weekday + 2, slot)
                                found = True
                                slot = adjust_slot(slot, course)
                                break
                            
                        # Increment week
                        week += 1

            # When a Course has not been scheduled, it cannot be put anywhere in any of the currently available rooms.
            # Therefore, a new room must be created. 
            if not found:

                # Creating Lecture or Lab, depending on the Course.
                if course.requires_lab:
                    new_room = Room("Extra Lab Room " + str(extra_lab_num) , cohort.room_size, True)
                    extra_lab_num += 1
                    labs.append(new_room)
                else:
                    new_room = Room("Extra Lecture Room " + str(extra_lec_num), cohort.room_size, False)
                    extra_lec_num += 1
                    lectures.append(new_room)
                
                # Ensuring Correct Weekday.
                if course in GENERAL:
                    weekday = 0
                    
                else:
                    weekday = 1
                
                week = 0
                # Monday/Wednesday Scanning and Placement
                while week < WEEKS:
                        
                    # First day scan (Monday/Tuesday)
                    if room.scan(course, week, weekday, slot) and cohort.scan(course, week, weekday, slot):
                            room.update_schedule(course, cohort, week, weekday, slot)
                            cohort.update_schedule(course, room, week, weekday, slot)
                            found = True
                            slot = adjust_slot(slot, course)
                            break
                        
                    # Second day scan (Wedensday/Thursday)
                    if room.scan(course, week, weekday + 2, slot) and cohort.scan(course, week, weekday + 2, slot):
                            room.update_schedule(course, cohort, week, weekday + 2, slot)
                            cohort.update_schedule(course, room, week, weekday + 2, slot)
                            found = True
                            slot = adjust_slot(slot, course)
                            break
                        
                    # Increment week
                    week += 1

                # Slot adjustment
                slot = adjust_slot(slot, course)

                
    all_rooms = lectures + labs

    for i in all_rooms:
        if i.is_empty == False:
            all_rooms.remove(i)

    return all_rooms  #, cohorts


# Testing code.
"""
if __name__ == "__main__":

    Lecture_1 = Room("Lecture", 30, False)
    Lab_1 = Room("Lab", 30, True)
    
    rooms_ = [Lab_1, Lecture_1]

    print(rooms_)

    all_cohorts = [Cohort("FS_1", 28, 1), Cohort("PCOM_1", 27, 1), Cohort("BA_1", 29, 1), Cohort("DXD_1", 40, 1)]

    final_rooms, final_cohorts = algorithm(all_cohorts, rooms_)

    final_rooms[0].print_schedule()

    final_cohorts[0].print_schedule()
"""



