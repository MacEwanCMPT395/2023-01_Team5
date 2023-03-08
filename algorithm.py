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

            # Find correct room type
            available_rooms = lectures
            if course.requires_lab:
                available_rooms = labs

            # Find correct room size
            for room in available_rooms:
                if cohort.room_size == room.capacity:
                    # Insert into correct Weekday.
                    if course in GENERAL:
                        # Monday/Wednesday Placement
                        room.update_schedule(course, 0, 0, slot)
                        if course.slot_type == 1:
                            slot += 3
                        else:
                            slot += course.slot_type * 2
                        # room.general_queue.append(course)
                    else:
                        # Tuesday/Thursday Placement
                        room.update_schedule(course, 0, 1, slot)
                        if course.slot_type == 1:
                            slot += 3
                        else:
                            slot += course.slot_type * 2
                        # room.special_queue.append(course)

    all_rooms = lectures + labs
    return all_rooms
    """
    
    ### Scheduling of courses from queues.
    for room in all_rooms:
    """




# Testing code.
if __name__ == "__main__":

    rooms_ = [Computer_Lab, Room_8]
    all_cohorts = [Cohort("FS_1", 28, 1), Cohort("PCOM_1", 27, 1), Cohort("BA_1", 29, 1)]

    algorithm(all_cohorts, rooms_)

    Room_8.print_schedule()
    Computer_Lab.print_schedule()

