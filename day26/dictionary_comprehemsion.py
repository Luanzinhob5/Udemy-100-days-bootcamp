import random
names = ["Alex","Beth","Caroline","Dave","Elanor","Freddie"]
student_score = {student: random.randint(1, 100)  for student in names}
print(student_score)

passed_students = {student: score for (student,score) in student_score.items() if score >= 60}
print(passed_students)
