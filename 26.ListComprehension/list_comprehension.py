import random

new_list = [i * 2 for i in range(1, 5)]
print(new_list)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
caps_names = [name.upper() for name in names if len(name) > 5]
print(caps_names)

students_scores = {student: random.randint(1, 100) for student in names}
passed_students = {student: score for (student, score) in students_scores.items() if score >= 60}
print(passed_students)

