import collections
import doctest
import os  # For check the path

preferred_rankings_student = {}
preferred_rankings_university = {}

free_student = []
tentative_acceptance = []

'''Initializes the students'''


def init_free_student() -> None:
    for student in preferred_rankings_student.keys():
        free_student.append(student)


'''Matching algorithm until stable match terminates'''


def stable_matching() -> None:
    while len(free_student) > 0:
        for student in free_student:
            begin_matching(student)


'''Find the first free woman available to a man at any given time'''


def begin_matching(student: str) -> None:
    print("DEALING WITH %s" % student)
    for university in preferred_rankings_student[student]:

        # Boolean for whether university is taken or not
        taken_match = [couple for couple in tentative_acceptance if university in couple]

        if len(taken_match) == 0:
            # tentatively acceptance the student and university
            tentative_acceptance.append([student, university])
            free_student.remove(student)
            print('%s is no longer a free student and is now tentatively acceptance to %s' % (student, university))
            break
        elif len(taken_match) > 0:
            print('%s is taken already..' % university)

            # Check ranking of the current student and the ranking of the 'to-be' student
            current_university = preferred_rankings_university[university].index(taken_match[0][0])
            potential_university = preferred_rankings_university[university].index(student)

            if current_university < potential_university:
                print('She\'s satisfied with %s..' % (taken_match[0][0]))
            else:
                print('%s is better than %s' % (student, taken_match[0][0]))
                print('Making %s free again.. and tentatively engaging %s and %s' % (
                    taken_match[0][0], student, university))

                # The new student is acceptance
                free_student.remove(student)

                # The old student is now free
                free_student.append(taken_match[0][0])

                # Update the student of the university (tentatively)
                taken_match[0][0] = student
                break


def init_dicts(path: str):
    have_dict_student = False
    have_dict_university = False
    if os.path.exists(path):  # Path is good
        with open(path) as file:

            while True:
                line = file.readline()
                if not line:
                    break
                if have_dict_student and have_dict_university:
                    break
                if "student" in line or "Student" in line:
                    have_dict_student = True
                    line = file.readline()
                    while line != "\n":
                        # get key
                        key = line.split(":")[0].strip()
                        # get value
                        preference_student_first = line.split(":")[1].strip(' [ ]\n')
                        preference_student_second = preference_student_first.split(",")
                        preference_student_list = []
                        for x in range(len(preference_student_second)):
                            preference_student_list.append(preference_student_second[x])
                        preferred_rankings_student.update({key: preference_student_list})
                        line = file.readline()
                if "university" in line or "University" in line:
                    have_dict_university = True
                    line = file.readline()
                    while line != "\n":
                        if line == '':
                            break
                        # get key
                        key = line.split(":")[0].strip()
                        # get value
                        preference_university_first = line.split(":")[1].strip(' [ ]\n')
                        preference_university_second = preference_university_first.split(",")
                        preference_university_list = []
                        for x in range(len(preference_university_second)):
                            preference_university_list.append(preference_university_second[x])
                        preferred_rankings_university.update({key: preference_university_list})
                        line = file.readline()


def activate_all_func():
    init_free_student()
    print(free_student)
    stable_matching()
    print(tentative_acceptance)
