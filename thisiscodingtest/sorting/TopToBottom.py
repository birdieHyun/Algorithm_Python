number_count = int(input())

array = []

for _ in range(number_count):
    array.append(int(input()))

answer = sorted(array, reverse = True)

print(answer)