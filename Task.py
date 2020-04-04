import random
import Student
from queue import LifoQueue
from _collections import deque


def create_student_file(new_file):
    open(new_file, 'w')


def add_random_student_data(filename, names, number_of_students):
    file = open(filename, 'w')
    for i in range(number_of_students):
        student_name = random.choice(names)
        student_identity = random.randrange(9000000, 9999999)
        file.write(student_name + ' ' + str(student_identity) + '\n')
    pass


def create_random_student_list(filename, number_of_students_on_list):
    student_list = []
    file = open(filename, 'r')
    total_lines = file.readlines()
    for i in range(number_of_students_on_list):
        pick = random.randint(0, len(total_lines)-1)
        line = total_lines[pick]
        line = line.split(' ')
        student = Student.Student(line[0], int(line[1]))
        student_list.append(student)
    return student_list


def remove_duplicate_students(student_list):
    unique = []
    unique_student = []
    for i in range(len(student_list)):
        student = student_list[i]
        if student.getidentity() not in unique:
            unique.append(student.getidentity())
            unique_student.append(student)
    return unique_student


def sort_student_list_with_student_identity(student_list):
    student_list.sort(key=lambda student: student.identity, reverse=True)
    student_list = sorted(student_list, key=lambda student: student.identity, reverse=False)
    return student_list

def push_student_list_to_stack(student_list):
    student_stack = LifoQueue(maxsize=len(student_list))
    for i in range(len(student_list)):
        student_stack.put(student_list[i])
    return student_stack

def push_to_stack_using_deque(student_list):
    student_stack = deque()
    for i in range(len(student_list)):
        student_stack.append(student_list[i])
    return student_stack