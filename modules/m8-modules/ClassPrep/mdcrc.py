"""This module contains data and function relative to MDCRC 6521 course"""

import random
# just an interesting number
Chapernowne_number = 0.12345678910111213141516171819202122232425
students = \
    ["Samuel", "Tyler", "Helen", "Nickolas", "Matthew", "Scott",
     "Schuyler", "Nicole", "Sai", "Melissa", "Clifford", "Paris"]
teachers = ["Brian", "Tom", "Eric"]


def selectStudentWithReplacement(students):
    """randomly select student from list students"""
    return random.choice(students)

def shufflePopStudents(students):
    """randomly select and remove a student from the list of students"""
    try:
        random.shuffle(students)
        return students.pop()
    except IndexError:
        return ""

def pair_groups(n_groups = 6):
    """ create a random pairing of the homework groups"""
    def _shuffle_pop(group1, groups):
        random.shuffle(groups)
        if groups[-1] != group1:
            match = groups.pop()
            return match, groups
        else:
            return _shuffle_pop(group1,groups)
    first = range(1,n_groups+1)
    second = first[:]
    return [(group,_shuffle_pop(group,second)) for group in first]

print("this is mdcrc.py")
