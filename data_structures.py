import math


# Setting Global Variables.
WEEKDAY_NAMES = ["Mon", "Tue", "Wed", "Thu"]
WEEKS = 15
DAYS = 4


class Cohort:
    def __init__(self, name, size, term):

        # Program name and term number.
        self.name = name
        self.term = term

        # 3 Dimensional List, containing entire Cohort schedule. Filled with Nones.
        self.schedule = []
        for week in range(0, WEEKS):
            self.schedule.append([])
            for weekday in range(0, DAYS):
                self.schedule[week].append([])
                for timeslot in range(0, 25):
                    self.schedule[week][weekday].append(None)

        # Finding Courses for Cohort.
        self.courses = set_courses(term, name[0:2])

        # Finding ideal room size for Cohort.
        sizes = [24, 30, 36, 40]
        self.size = size
        for s in sizes:
            if size > s:
                continue
            else:
                self.room_size = s
                break

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    def update_schedule(self, course, room, week, day, slot):
        # Conversions for certain cases.
        if course.slot_type == 1:
            slot_type = 1.5
            weekly_hours = 3
        elif course.slot_type == 2:
            slot_type = 2
            weekly_hours = 4
        elif course.slot_type == 3:
            slot_type = 3
            weekly_hours = 6
        else:
            raise Exception("Invalid slot Type.")

        # This integer represents how long each Course session is, in half hours.
        course_duration = int(slot_type * 2)
        # This number represents how many sessions each course runs for.
        sessions = math.ceil(course.hours / weekly_hours)

        # Placement of Course within Room schedule.
        for w in range(0, sessions):
            for t in range(slot, course_duration):
                if self.schedule[week + w][day][slot + t] is None:
                    self.schedule[week + w][day][slot + t] = f"{course.name} / {room.room_number}"
                else:
                    raise Exception("Schedule Conflict.")
        # If the course runs twice a week, which only occurs with slot_type 1, update the schedule.
        for w in range(0, sessions):
            for t in range(slot, course_duration):
                if self.schedule[week + w][day + 2][slot + t] is None:
                    self.schedule[week + w][day + 2][slot + t] = f"{course.name} / {room.room_number}"
                else:
                    raise Exception("Schedule Conflict.")

    def print_schedule(self):
        # Displays Room Schedule, in an ideal format.
        w = 0
        print(self)
        for week in self.schedule:
            print(f"Week {w + 1}:")
            w += 1
            d = 0
            for weekday in week:
                print(f"\t{WEEKDAY_NAMES[d]}: ", end='')
                print(weekday)
                d += 1

    def scan(self, course, week, day, slot):
        # Conversions for certain cases.
        if course.slot_type == 1:
            slot_type = 1.5
            weekly_hours = 3
        elif course.slot_type == 2:
            slot_type = 2
            weekly_hours = 4
        elif course.slot_type == 3:
            slot_type = 3
            weekly_hours = 6
        else:
            raise Exception("Invalid slot Type.")

        # This integer represents how long each Course session is, in half hours.
        course_duration = int(slot_type * 2)
        # This number represents how many sessions each course runs for.
        sessions = math.ceil(course.hours / weekly_hours)

        # Placement of Course within Room schedule.
        for w in range(0, sessions):
            for t in range(slot, course_duration):
                if w + week < WEEKS and self.schedule[week + w][day][slot + t] is None:
                    continue
                else:
                    return False

        # If the course runs twice a week update the schedule.
        if course.slot_type == 1 or course.slot_type == 2:
            for w in range(0, sessions):
                for t in range(slot, course_duration):
                    if self.schedule[week + w][day + 2][slot + t] is None:
                        continue
                    else:
                        return False
        return True

class Room:
    def __init__(self, room_number, capacity, is_lab):
        # Identifying number for room (str).
        self.room_number = room_number
        # Maximum Student capacity of room (int).
        self.capacity = capacity
        # Lab Status (boolean).
        self.is_lab = is_lab

        # Separate class queues for Mon/Wed and Tue/Thu.

        self.general_queue = []
        self.special_queue = []

        # Labs and Lecture Rooms have different times they are open. Reflect this with the amount of timeslots.
        if is_lab:
            spaces = 25
        else:
            spaces = 18

        # 3 Dimensional List, containing entire Term schedule. Filled with Nones.
        self.schedule = []
        for week in range(0, WEEKS):
            self.schedule.append([])
            for weekday in range(0, DAYS):
                self.schedule[week].append([])
                for timeslot in range(0, spaces):
                    self.schedule[week][weekday].append(None)
        '''
        Visual Representation
        [ # Room Term Schedule, Consists of 13 Weeks
            [ # Week, Consists of 4 Weekdays
                [ # Weekday, A list which contains 25 elements for classes, which represent 30 minute periods. 
                   MATH_114, MATH_114, CMPT_101, CMPT_101, # Timeslots, Courses which run.
                ]
            ]
        ]
        '''

    def __repr__(self):
        return self.room_number

    def __str__(self):
        return self.room_number

    def print_schedule(self):
        # Displays Room Schedule, in an ideal format.
        w = 0
        print(self)
        for week in self.schedule:
            print(f"Week {w + 1}:")
            w += 1
            d = 0
            for weekday in week:
                print(f"\t{WEEKDAY_NAMES[d]}: ", end='')
                print(weekday)
                d += 1

    def update_schedule(self, course, cohort, week, day, slot):
        # Conversions for certain cases.
        if course.slot_type == 1:
            slot_type = 1.5
            weekly_hours = 3
        elif course.slot_type == 2:
            slot_type = 2
            weekly_hours = 4
        elif course.slot_type == 3:
            slot_type = 3
            weekly_hours = 6
        else:
            raise Exception("Invalid slot Type.")

        # This integer represents how long each Course session is, in half hours.
        course_duration = int(slot_type * 2)
        # This number represents how many sessions each course runs for.
        sessions = math.ceil(course.hours / weekly_hours)

        # Placement of Course within Room schedule.
        for w in range(0, sessions):
            for t in range(slot, course_duration):
                if self.schedule[week + w][day][slot + t] is None:
                    self.schedule[week + w][day][slot + t] = f"{course.name} / {cohort.name}"
                else:
                    raise Exception("Schedule Conflict.")

        # If the course runs twice a week, which only occurs with slot_type 1, update the schedule.
        for w in range(0, sessions):
            for t in range(slot, course_duration):
                if self.schedule[week + w][day + 2][slot + t] is None:
                    self.schedule[week + w][day + 2][slot + t] = f"{course.name} / {cohort.name}"
                else:
                    raise Exception("Schedule Conflict.")

    def scan(self, course, week, day, slot):
        # Conversions for certain cases.
        if course.slot_type == 1:
            slot_type = 1.5
            weekly_hours = 3
        elif course.slot_type == 2:
            slot_type = 2
            weekly_hours = 4
        elif course.slot_type == 3:
            slot_type = 3
            weekly_hours = 6
        else:
            raise Exception("Invalid slot Type.")

        # This integer represents how long each Course session is, in half hours.
        course_duration = int(slot_type * 2)
        # This number represents how many sessions each course runs for.
        sessions = math.ceil(course.hours / weekly_hours)

        # Placement of Course within Room schedule.
        for w in range(0, sessions):
            for t in range(slot, course_duration):
                if w + week < WEEKS and self.schedule[week + w][day][slot + t] is None:
                    continue
                else:
                    return False

        # If the course runs twice a week update the schedule.
        if course.slot_type == 1 or course.slot_type == 2:
            for w in range(0, sessions):
                for t in range(slot, course_duration):
                    if self.schedule[week + w][day + 2][slot + t] is None:
                        continue
                    else:
                        return False
        return True

class Course:
    def __init__(self, name, hours, requires_lab, slot_type):

        # Shorthand Course name. (e.g. "CMSK 0150")
        self.name = name

        # Integer of Transcript course running hours.
        self.hours = hours

        # Boolean for requires lab
        self.requires_lab = requires_lab

        self.slot_type = slot_type

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


def set_courses(term, program):
    if term == 1:
        if program == "PC":
            return PCOM_TERM_1
        elif program == "BC":
            return BCOM_TERM_1
        elif program == "PM":
            return PM_TERM_1
        elif program == "BA":
            return BA_TERM_1
        elif program == "GL":
            return GL_TERM_1
        elif program == "DX":
            return DXDI_TERM_1
        elif program == "FS":
            return FS_TERM_1
        elif program == "BK":
            return BK_TERM_1
    elif term == 2:
        if program == "PC":
            return PCOM_TERM_2
        elif program == "BC":
            return BCOM_TERM_2
        elif program == "PM":
            return PM_TERM_2
        elif program == "BA":
            return BA_TERM_2
        elif program == "GL":
            return GL_TERM_2
        elif program == "DX":
            return DXDI_TERM_2
        elif program == "FS":
            return FS_TERM_2
        elif program == "BK":
            return BK_TERM_2
    elif term == 3:
        if program == "PC":
            return PCOM_TERM_3
        elif program == "BC":
            return BCOM_TERM_3
        elif program == "PM":
            return PM_TERM_3
        elif program == "BA":
            return BA_TERM_3
        elif program == "GL":
            return GL_TERM_3
        elif program == "DX":
            return DXDI_TERM_3
        elif program == "FS":
            return FS_TERM_3
        elif program == "BK":
            return BK_TERM_3

# Professional Communication (PCOM)
# Term 1
PCOM_0101 = Course("PCOM_0101", 35, False, 1)
PCOM_0105 = Course("PCOM_0105", 35, False, 1)
PCOM_0107 = Course("PCOM_0107", 18, True, 1)
CMSK_0233 = Course("CMSK_0233", 7, True, 1)
CMSK_0235 = Course("CMSK_0235", 6, True, 1)
PCOM_TERM_1 = [PCOM_0101, PCOM_0105, PCOM_0107, CMSK_0233, CMSK_0235]
# Term 2
PCOM_0102 = Course("PCOM_0102", 35, False, 1)
PCOM_0201 = Course("PCOM_0201", 35, False, 1)
PCOM_0108 = Course("PCOM_0108", 18, True, 1)
PCOM_TERM_2 = [PCOM_0102, PCOM_0201, PCOM_0108]
# Term 3
PCOM_0202 = Course("PCOM_0202", 33, False, 1)
PCOM_0103 = Course("PCOM_0103", 35, False, 1)
PCOM_0109 = Course("PCOM_0109", 14, True, 2)  # WARNING, THIS COURSE IS INACCURATE.
PCOM_TERM_3 = [PCOM_0102, PCOM_0201, PCOM_0109]

# Business Communication (BCOM)
# Term 1
PCOM_0203 = Course("PCOM_0203", 15, False, 1)
SUPR_0751 = Course("SUPR_0751", 7, False, 2)
PCOM_0204 = Course("PCOM_0204", 35, False, 1)
CMSK_0237 = Course("CMSK_0237", 12, False, 1)  # Online?
SUPR_0837 = Course("SUPR_0837", 7, False, 2)
SUPR_0841 = Course("SUPR_0841", 7, False, 2)
BCOM_TERM_1 = [PCOM_0203, SUPR_0751, PCOM_0204, CMSK_0237, SUPR_0837, SUPR_0841]
# Term 2
SUPR_0821 = Course("SUPR_0821", 7, False, 2)
SUPR_0822 = Course("SUPR_0822", 7, False, 2)
SUPR_0718 = Course("SUPR_0718", 7, False, 2)
SUPR_0836 = Course("SUPR_0836", 7, False, 2)
AVDM_0199 = Course("AVDM_0199", 3, False, 1)  # Online?
PCOM_0106 = Course("PCOM_0106", 35, False, 2)
BCOM_TERM_2 = [SUPR_0821, SUPR_0822, SUPR_0836, SUPR_0836, AVDM_0199, PCOM_0106]
# Term 3
PCOM_0205 = Course("PCOM_0205", 30, False, 3)
PCOM_TBD = Course("PCOM_TBD", 21, False, 1)
PCOM_0207 = Course("PCOM_0207", 6, False, 2)
SUPR_0863 = Course("SUPR_863", 7, False, 2)
PCOM_0206 = Course("PCOM_0206", 6, False, 3)
AVDM_0260 = Course("AVDM_0260", 6, False, 1)  # Online?
BCOM_TERM_3 = [PCOM_0205, PCOM_TBD, PCOM_0207, SUPR_0863, PCOM_0206, AVDM_0260]

GENERAL = [PCOM_0101, PCOM_0105, PCOM_0107, CMSK_0233, CMSK_0235, PCOM_0102, PCOM_0201, PCOM_0108, PCOM_0102, PCOM_0201,
           PCOM_0109, PCOM_0203, SUPR_0751, PCOM_0204, CMSK_0237, SUPR_0837, SUPR_0841, SUPR_0821, SUPR_0822, SUPR_0836,
           SUPR_0836, AVDM_0199, PCOM_0106, PCOM_0205, PCOM_TBD, PCOM_0207, SUPR_0863, PCOM_0206, AVDM_0260]

# Full Stack Web Development (FS)
# Term 1
CMSK_0150 = Course("CMSK_0150", 16, True, 2)
CMSK_0151 = Course("CMSK_0151", 16, True, 2)
CMSK_0152 = Course("CMSK_0152", 16, True, 2)
CMSK_0157 = Course("CMSK_0157", 16, True, 2)
CMSK_0154 = Course("CMSK_0154", 16, True, 2)
FS_TERM_1 = [CMSK_0150, CMSK_0151, CMSK_0152, CMSK_0154, CMSK_0157]
# Term 2
CMSK_0153 = Course("CMSK_0153", 18, True, 2)
CMSK_0200 = Course("CMSK_0200", 16, True, 2)
CMSK_0201 = Course("CMSK_0201", 18, True, 2)
CMSK_0203 = Course("CMSK_0203", 16, True, 2)
CMSK_0160 = Course("CMSK_0160", 18, True, 2)
FS_TERM_2 = [CMSK_0153, CMSK_0200, CMSK_0201, CMSK_0203, CMSK_0160]
# Term 3
PCOM_0160 = Course("PCOM_0160", 50, True, 2)
FS_TERM_3 = [PCOM_0160]

# Digital Design (DXDI)
# Term 1
AVDM_0165 = Course("AVDM_0165", 18, True, 1)
DXDI_0101 = Course("DXDI_0101", 24, True, 1)
DXDI_0102 = Course("DXDI_0102", 24, True, 1)
DXDI_TERM_1 = [AVDM_0165, DXDI_0101, DXDI_0102]
# Term 2
AVDM_0170 = Course("AVDM_0170", 18, True, 1)
AVDM_0138 = Course("AVDM_0138", 18, True, 1)
DXDI_0103 = Course("DXDI_0103", 24, True, 1)
DXDI_0104 = Course("DXDI_0104", 24, True, 1)
DXDI_TERM_2 = [AVDM_0170, AVDM_0138, DXDI_0103, DXDI_0104]
# Term 3
AVDM_0238 = Course("AVDM_0238", 18, True, 1)
AVDM_0270 = Course("AVDM_0270", 18, True, 1)
DXDI_9901 = Course("DXDI_0991", 45, True, 1)
DXDI_TERM_3 = [AVDM_0238, AVDM_0270, DXDI_9901]


# Bookkeeping (BK)
# Term 1
ACCT_0201 = Course("ACCT_0201", 18, False, 1)
ACCT_0202 = Course("ACCT_0202", 12, False, 1)
ACCT_0203 = Course("ACCT_0203", 12, False, 1)
BK_TERM_1 = [ACCT_0201, ACCT_0202, ACCT_0203]
# Term 2
ACCT_0206 = Course("ACCT_0206", 12, False, 1)
ACCT_0210 = Course("ACCT_0210", 28, True, 1)
ACCT_0211 = Course("ACCT_0211", 28, True, 1)
BK_TERM_2 = [ACCT_0206, ACCT_0210, ACCT_0211]
# Term 3
ACCT_0208 = Course("ACCT_0208", 21, True, 1)
ACCT_9901 = Course("ACCT_9901", 33, True, 1)
BK_TERM_3 = [ACCT_0208, ACCT_9901]

# Supply Chain Management (GLM)
# Term 1
SCMT_0501 = Course("SCMT_0501", 21, False, 1)
SCMT_0502 = Course("SCMT_0502", 21, False, 1)
PRDV_0304 = Course("PRDV_0304", 15, False, 1)
# SCMT_9901?
GL_TERM_1 = [SCMT_0501, SCMT_0502, PRDV_0304]
# Term 2
SCMT_0503 = Course("SCMT_0503", 15, False, 1)
SCMT_0504 = Course("SCMT_0504", 21, False, 1)
# SCMT_9902?
GL_TERM_2 = [SCMT_0503, SCMT_0504]
# Term 3
SCMT_0505 = Course("SCMT_0505", 21, False, 1)
PCOM_0151 = Course("PCOM_0151", 39, False, 3)  # 13 Sessions, 3 Hours Each
GL_TERM_3 = [SCMT_0505, PCOM_0151]


# Business Analysis (BA)
# Term 1
PRDV_0640 = Course("PRDV_0640", 21, False, 1)
PRDV_0652 = Course("PRDV_0652", 14, False, 1)
PRDV_0653 = Course("PRDV_0653", 21, False, 1)
PRDV_0642 = Course("PRDV_0642", 14, False, 1)
BA_TERM_1 = [PRDV_0640, PRDV_0652, PRDV_0653, PRDV_0642]
# Term 2
PRDV_0644 = Course("PRDV_0644", 21, False, 1)
PRDV_0648 = Course("PRDV_0648", 12, False, 1)
PCOM_0140 = Course("PCOM_0140", 35, False, 1)
BA_TERM_2 = [PRDV_0644, PRDV_0648, PCOM_0140]
# Term 3
PRDV_0646 = Course("PRDV_0646", 14, False, 1)
PCOM_0141 = Course("PCOM_0141", 39, False, 3)  # 13 Sessions, 3 Hours Each.
BA_TERM_3 = [PRDV_0646, PCOM_0141]


# Project Management (PM)
# Term 1
PRDV_0201 = Course("PRDV_0201", 21, False, 1)
PRDV_0202 = Course("PRDV_0202", 14, False, 1)
PRDV_0203 = Course("PRDV_0203", 21, False, 1)
PM_TERM_1 = [PRDV_0201, PRDV_0202, PRDV_0203]
# Term 2
PRDV_0204 = Course("PRDV_0204", 14, False, 1)
PRDV_0205 = Course("PRDV_0205", 21, False, 1)
PCOM_0130 = Course("PCOM_0130", 21, False, 1)
PRDV_0206 = Course("PRDV_0206", 14, False, 1)
PM_TERM_2 = [PRDV_0204, PRDV_0205, PCOM_0130, PRDV_0206]
# Term 3
PRDV_0207 = Course("PRDV_0207", 14, False, 1)
PCOM_0131 = Course("PCOM_0131", 39, False, 3)
PM_TERM_3 = [PRDV_0207, PCOM_0131]

# Creation of Default Available Rooms.
Room_1 = Room("11-533", 36, False)
Room_2 = Room("11-534", 36, False)
Room_3 = Room("11-560", 24, False)
Room_4 = Room("11-562", 24, False)
Room_5 = Room("11-564", 24, False)
Room_6 = Room("11-458", 40, False)
Room_7 = Room("11-430", 30, False)
Room_8 = Room("11-320", 30, False)
Computer_Lab = Room("11-532", 30, True)
ROOMS = [Room_1, Room_2, Room_3, Room_4, Room_5, Room_6, Room_7, Room_8, Computer_Lab]
"""
if __name__ == "__main__":
    Computer_Lab.update_schedule(CMSK_0150, 0, 0, 0)
    Computer_Lab.update_schedule(ACCT_0202, 0, 1, 0)
    Computer_Lab.update_schedule(DXDI_0101, 0, 0, 4)
    Computer_Lab.print_schedule()
"""

