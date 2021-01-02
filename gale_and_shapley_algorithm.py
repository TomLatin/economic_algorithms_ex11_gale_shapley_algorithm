import collections
import doctest

# The university that the student prefer
preferred_rankings_student = {
    'ryan': ['Yale', 'Harvard', 'NYU', 'MIT'],
    'josh': ['Harvard', 'Yale', 'MIT', 'NYU'],
    'blake': ['Harvard', 'MIT', 'NYU', 'Yale'],
    'connor': ['Yale', 'Harvard', 'NYU', 'MIT']
}

# The student that the university prefer
preferred_rankings_university = {
    'Yale': ['ryan', 'blake', 'josh', 'connor'],
    'Harvard': ['ryan', 'blake', 'connor', 'josh'],
    'NYU': ['connor', 'josh', 'ryan', 'blake'],
    'MIT': ['ryan', 'josh', 'connor', 'blake']
}


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
                print('Making %s free again.. and tentatively engaging %s and %s' % (taken_match[0][0], student, university))

                # The new student is acceptance
                free_student.remove(student)

                # The old student is now free
                free_student.append(taken_match[0][0])

                # Update the student of the university (tentatively)
                taken_match[0][0] = student
                break


if __name__ == "__main__":
    init_free_student()
    print(free_student)
    stable_matching()
    print(tentative_acceptance)
