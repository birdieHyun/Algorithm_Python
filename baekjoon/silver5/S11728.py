a = input()

N = list(map(int, input().split()))
M = list(map(int, input().split()))

answer = N + M
answer.sort()

print(*answer)

for i in answer:
    print(i)
