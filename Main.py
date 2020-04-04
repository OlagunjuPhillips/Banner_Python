from collections import deque

import Student
import Task

names = ['James', 'John', 'Kate', 'Thomas', 'Peter', 'Simeone', 'Geralt']
filename = 'student_data.txt'
number_of_students = 3000
number_of_students_on_list = 100

Task.create_student_file(filename)
Task.add_random_student_data(filename, names, number_of_students)

student_list = Task.create_random_student_list(filename, number_of_students_on_list)

student_list = Task.remove_duplicate_students(student_list)

student_list = Task.sort_student_list_with_student_identity(student_list)

student_stack = Task.push_student_list_to_stack(student_list)

student_stack_using_deque: deque[Student] = Task.push_to_stack_using_deque(student_list)


