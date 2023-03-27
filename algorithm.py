from data_structures import *


def find_room(all_rooms):
    for room in all_rooms:
        if room.capacity == room.capacity:
            return room
        else:
            continue


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

    ### Queuing Courses
    ## Finding Rooms for Courses
    # Goes through each cohort
    for cohort in cohorts:
        slot = 0
        # Goes through each course in each cohort.
        for course in cohort.courses:  # Each course needs to be placed correctly.
            week = 0
            # Find correct room type
            available_rooms = lectures
            if course.requires_lab:
                available_rooms = labs


            found = False
            # Find correct room size
            for room in available_rooms:
                if cohort.room_size == room.capacity:
                    # Insert into correct Weekday.
                    if course in GENERAL:

                        # Monday/Wednesday Scanning and Placement
                        while week < WEEKS:

                            if room.scan(course, week, 0, slot):
                                if cohort.scan(course, week, 0, slot):
                                    room.update_schedule(course, cohort, week, 0, slot)
                                    cohort.update_schedule(course, room, week, 0, slot)
                                    found = True
                                    # Adjusting slot placement
                                    if course.slot_type == 1:
                                        slot += 3
                                    else:
                                        slot += course.slot_type * 2
                                    break

                            if room.scan(course, week, 2, slot):
                                if cohort.scan(course, week, 2, slot):
                                    room.update_schedule(course, cohort, week, 2, slot)
                                    cohort.update_schedule(course, room, week, 2, slot)
                                    found = True
                                    # Adjusting slot placement
                                    if course.slot_type == 1:
                                        slot += 3
                                    else:
                                        slot += course.slot_type * 2
                                    break
                            week += 1

                    else:
                        # Tuesday/Thursday Placement
                        while week < WEEKS:

                            if room.scan(course, week, 1, slot):
                                if cohort.scan(course, week, 1, slot):
                                    room.update_schedule(course, cohort, week, 1, slot)
                                    cohort.update_schedule(course, room, week, 1, slot)
                                    found = True
                                    # Adjusting slot placement
                                    if course.slot_type == 1:
                                        slot += 3
                                    else:
                                        slot += course.slot_type * 2
                                    break
                                week += 1

                            if room.scan(course, week, 3, slot):
                                if cohort.scan(course, week, 3, slot):
                                    room.update_schedule(course, cohort, week, 3, slot)
                                    cohort.update_schedule(course, room, week, 3, slot)

                                    # Adjusting slot placement
                                    if course.slot_type == 1:
                                        slot += 3
                                    else:
                                        slot += course.slot_type * 2
                                    break
                            week += 1

            if not found:
                if course.requires_lab:
                    new_room = Room("Extra lab", cohort.room_size, True)
                else:
                    new_room = Room("Extra lecture", cohort.room_size, False)

                if course in GENERAL:
                    new_room.update_schedule(course, cohort, 0, 0, slot)
                    cohort.update_schedule(course, new_room, 0, 0, slot)
                    labs.append(new_room)
                else:
                    new_room.update_schedule(course, cohort, 0, 1, slot)
                    cohort.update_schedule(course, new_room, 0, 1, slot)
                    lectures.append(new_room)
                if course.slot_type == 1:
                    slot += 3
                else:
                    slot += course.slot_type * 2

                
    all_rooms = lectures + labs
    return all_rooms


# Testing code.
if __name__ == "__main__":

    rooms_ = [Computer_Lab, Room_8]
    all_cohorts = [Cohort("FS_1", 28, 1), Cohort("PCOM_1", 27, 1), Cohort("BA_1", 29, 1), Cohort("DXD_1", 40, 1)]

    algorithm(all_cohorts, rooms_)

    all_cohorts[3].print_schedule()


