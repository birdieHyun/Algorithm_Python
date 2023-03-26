students_number =int(input())

students = []
dissatisfaction = 0

for i in range(students_number):
    students.append(int(input()))


students.sort()

for i in range(students_number):
    dissatisfaction += abs(students[i] - (i + 1))

print(dissatisfaction)

