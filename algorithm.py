from data_structures import *


# Start of algorithm.

def test(cohorts):
    # Finding Rooms for Cohorts (Needs to be expanded upon)
    for c in cohorts:
        for course in cohorts[c].courses:
            Computer_Lab.special_queue.append(course)
    
    # Scheduling of courses from queues.
    slot = 0
    for course in Computer_Lab.special_queue:
        Computer_Lab.update_schedule(course, 0, 0, 0 + slot, 1)
        slot += 3
    Computer_Lab.print_schedule()

