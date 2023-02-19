# 실전문제 큰 수의 법칙
size, multiple, repeat = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

first = data[size -1]
second = data[size -2]

answer = 0

for i in range(1,multiple + 1):
    if repeat % i == 0:
        answer += second
    else:
        answer += first

print(answer)