import math

WEEKDAY_NAMES = ["Mon", "Tue", "Wed", "Thu"]
WEEKS = 15
DAYS = 4


class Cohort:
    def __init__(self, name, size, term):

        self.name = name
        self.term = term
        # Finding Courses for Cohort.
        if term == 1:
            if name[0:2] == "PC":
                self.courses = PCOM_TERM_1
            elif name[0:2] == "BC":
                self.courses = BCOM_TERM_1
            elif name[0:2] == "PM":
                self.courses = PM_TERM_1
            elif name[0:2] == "BA":
                self.courses = BA_TERM_1
            elif name[0:2] == "GL":
                self.courses = GL_TERM_1
            elif name[0:2] == "DX":
                self.courses = DXDI_TERM_1
            elif name[0:2] == "FS":
                self.courses = FS_TERM_1
            elif name[0:2] == "BK":
                self.courses = BK_TERM_1

        elif term == 2:
            pass
        elif term == 3:
            pass

        

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


class Room:
    def __init__(self, room_number, capacity, is_lab):

        # Identifying number for room (str).
        self.room_number = room_number
        # Maximum Student capacity of room (int).
        self.capacity = capacity
        # Lab Status (boolean).
        self.is_lab = is_lab

        self.general_queue = []
        self.special_queue = []

        # Labs and Lecture Rooms have different times they are open. Reflect this with the amount of timeslots.
        if is_lab:
            slots = 25
        else:
            slots = 18

        # 3 Dimensional List, containing entire Term schedule. Filled with Nones.
        self.schedule = []
        for week in range(0, WEEKS):
            self.schedule.append([])
            for weekday in range(0, DAYS):
                self.schedule[week].append([])
                for timeslot in range(0, slots):
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

    def update_schedule(self, course, week, day, slot, slot_type):
        # Conversions for certain cases.
        if slot_type == 1:
            slot_type = 1.5
            weekly_hours = 3
        elif slot_type == 2:
            weekly_hours = 4
        elif slot_type == 3:
            weekly_hours = 6
        else:
            raise Exception("Invalid slot Type.")

        # This integer represents how long each Course session is, in half hours.
        course_duration = int(slot_type * 2)
        # This number represents how many sessions each course runs for.
        sessions = math.ceil(course.hours / weekly_hours)

        # Placement of Course within Room schedule.
        for w in range(0, sessions):
            for t in range(0, course_duration):
                if self.schedule[week + w][day][slot + t] is None:
                    self.schedule[week + w][day][slot + t] = course
                else:
                    raise Exception("Schedule Conflict.")
        # If the course runs twice a week, which only occurs with slot_type 1, update the schedule.
        for w in range(0, sessions):
            for t in range(0, course_duration):
                if self.schedule[week + w][day + 2][slot + t] is None:
                    self.schedule[week + w][day + 2][slot + t] = course
                else:
                    raise Exception("Schedule Conflict.")


class Course:
    def __init__(self, name, hours, requires_lab):

        # Shorthand Course name. (e.g. "CMSK 0150")
        self.name = name

        # Integer of Transcript course running hours.
        self.hours = hours

        # Boolean for requires lab
        self.requires_lab = requires_lab

        # Priority? Organization? Other Requirements?

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


# Professional Communication (PCOM)
# Term 1
PCOM_0101 = Course("PCOM_0101", 35, False)
PCOM_0105 = Course("PCOM_0105", 35, False)
PCOM_0107 = Course("PCOM_0107", 18, True)
CMSK_0233 = Course("CMSK_0233", 7, True)
CMSK_0235 = Course("CMSK_0235", 6, True)
PCOM_TERM_1 = [PCOM_0101, PCOM_0105, PCOM_0107, CMSK_0233, CMSK_0235]
# Term 2
PCOM_0102 = Course("PCOM_0102", 35, False)
PCOM_0201 = Course("PCOM_0201", 35, False)
PCOM_0108 = Course("PCOM_0108", 18, True)
PCOM_TERM_2 = [PCOM_0102, PCOM_0201, PCOM_0108]
# Term 3
PCOM_0202 = Course("PCOM_0202", 33, False)
PCOM_0103 = Course("PCOM_0103", 35, False)
PCOM_0109 = Course("PCOM_0109", 14, True)  # WARNING, THIS COURSE IS INACCURATE.
PCOM_TERM_3 = [PCOM_0102, PCOM_0201, PCOM_0109]

# Business Communication (BCOM)
# Term 1
PCOM_0203 = Course("PCOM_0203", 15, False)
SUPR_0751 = Course("SUPR_0751", 7, False)
PCOM_0204 = Course("PCOM_0204", 35, False)
CMSK_0237 = Course("CMSK_0237", 12, False)  # Online?
SUPR_0837 = Course("SUPR_0837", 7, False)
SUPR_0841 = Course("SUPR_0841", 7, False)
BCOM_TERM_1 = [PCOM_0203, SUPR_0751, PCOM_0204, CMSK_0237, SUPR_0837, SUPR_0841]
# Term 2
SUPR_0821 = Course("SUPR_0821", 7, False)
SUPR_0822 = Course("SUPR_0822", 7, False)
SUPR_0718 = Course("SUPR_0718", 7, False)
SUPR_0836 = Course("SUPR_0836", 7, False)
AVDM_0199 = Course("ACDM_0199", 3, False)  # Online?
PCOM_0106 = Course("PCOM_0106", 35, False)
BCOM_TERM_2 = [SUPR_0821, SUPR_0822, SUPR_0836, SUPR_0836, AVDM_0199, PCOM_0106]
# Term 3
PCOM_0205 = Course("PCOM_0205", 30, False)
PCOM_TBD = Course("PCOM_TBD", 21, False)
PCOM_0207 = Course("PCOM_0207", 6, False)
SUPR_0863 = Course("SUPR_863", 7, False)
PCOM_0206 = Course("PCOM_0206", 6, False)
AVDM_0260 = Course("AVDM_0260", 6, False)
BCOM_TERM_3 = [PCOM_0205, PCOM_TBD, PCOM_0207, SUPR_0863, PCOM_0206, AVDM_0260]

# Full Stack Web Development (FS)
# Term 1
CMSK_0150 = Course("CMSK_0150", 16, True)
CMSK_0151 = Course("CMSK_0151", 16, True)
CMSK_0152 = Course("CMSK_0152", 16, True)
CMSK_0157 = Course("CMSK_0157", 16, True)
CMSK_0154 = Course("CMSK_0154", 16, True)
FS_TERM_1 = [CMSK_0150, CMSK_0151, CMSK_0152, CMSK_0154, CMSK_0157]
# Term 2
CMSK_0153 = Course("CMSK_0153", 18, True)
CMSK_0200 = Course("CMSK_0200", 16, True)
CMSK_0201 = Course("CMSK_0201", 18, True)
CMSK_0203 = Course("CMSK_0203", 16, True)
CMSK_0160 = Course("CMSK_0160", 18, True)
FS_TERM_2 = [CMSK_0153, CMSK_0200, CMSK_0201, CMSK_0203, CMSK_0160]
# Term 3
PCOM_0160 = Course("PCOM_0160", 50, True)
FS_TERM_3 = [PCOM_0160]

# Digital Design (DXDI)
# Term 1
AVDM_0165 = Course("ACDM_0165", 18, True)
DXDI_0101 = Course("DXDI_0101", 24, True)
DXDI_0102 = Course("DXDI_0102", 24, True)
DXDI_TERM_1 = [AVDM_0165, DXDI_0101, DXDI_0102]


# Bookkeeping (BK)
# Term 1
ACCT_0201 = Course("ACCT_0201", 18, False)
ACCT_0202 = Course("ACCT_0202", 12, False)
ACCT_0203 = Course("ACCT_0203", 12, False)
BK_TERM_1 = [ACCT_0201, ACCT_0202, ACCT_0203]
# Term 2
ACCT_0206 = Course("ACCT_0206", 12, False)
ACCT_0210 = Course("ACCT_0210", 28, True)
ACCT_0211 = Course("ACCT_0211", 28, True)
BK_TERM_2 = [ACCT_0206, ACCT_0210, ACCT_0211]
# Term 3
ACCT_0208 = Course("ACCT_0208", 21, True)
ACCT_9901 = Course("ACCT_9901", 33, True)
BK_TERM_3 = [ACCT_0208, ACCT_9901]

# Supply Chain Management (GLM)
# Term 1
SCMT_0501 = Course("SCMT_0501", 21, False)
SCMT_0502 = Course("SCMT_0502", 21, False)
PRDV_0304 = Course("PRDV_0304", 15, False)
GL_TERM_1 = [SCMT_0501, SCMT_0502, PRDV_0304]
# SCMT_9901?
# Term 2 

# Business Analysis (BA)
# Term 1
PRDV_0640 = Course("PRDV_0640", 21, False)
PRDV_0652 = Course("PRDV_0652", 14, False)
PRDV_0653 = Course("PRDV_0653", 21, False)
PRDV_0642 = Course("PRDV_0642", 14, False)
BA_TERM_1 = [PRDV_0640, PRDV_0652, PRDV_0653, PRDV_0642]
# Term 2

# Project Management (PM)
# Term 1
PRDV_0201 = Course("PRDV_0201", 21, False)
PRDV_0202 = Course("PRDV_0202", 14, False)
PRDV_0203 = Course("PRDV_0203", 21, False)
PM_TERM_1 = [PRDV_0201, PRDV_0202, PRDV_0203]
# Term 2
PRDV_0204 = Course("PRDV_0204", 14, False)
PRDV_0205 = Course("PRDV_0205", 21, False)
PCOM_0130 = Course("PCOM_0130", 21, False)
PRDV_0206 = Course("PRDV_0206", 14, False)
PM_TERM_2 = [PRDV_0204, PRDV_0205, PCOM_0130, PRDV_0206]
# Term 3
PRDV_0207 = Course("PRDV_0207", 14, False)
PCOM_0131 = Course("PCOM_0131", 39, False)
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
"""
if __name__ == "__main__":
    Computer_Lab.update_schedule(CMSK_0150, 0, 0, 0, 1)
    Computer_Lab.update_schedule(ACCT_0202, 0, 1, 0, 2)
    Computer_Lab.update_schedule(DXDI_0101, 0, 0, 3, 3)
    Computer_Lab.print_schedule()
"""

