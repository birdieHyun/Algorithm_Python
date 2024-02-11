students_count =int(input())

students = []
dissatisfaction = 0

for i in range(students_count):
    students.append(int(input()))

students.sort()

for i in range(students_count):
    dissatisfaction += abs(students[i] - (i + 1))

print(dissatisfaction)
