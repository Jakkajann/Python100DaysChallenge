# Dictionary Comprehesion

import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

students_score = {student:random.randint(1,100) for student in names}

passed_students = {student:score for (student, score) in students_score.items() if score >= 60}

print(students_score)
print(passed_students)