import sys
input = sys.stdin.readline

N = int(input())
MAX = int(10000)

counting_sort = [0] * (MAX + 1)

for _ in range(N):
    tmp = int(input())
    counting_sort[tmp] += 1

for i in range(len(counting_sort)):
    if counting_sort[i] > 0:
        for j in range(counting_sort[i]):
            print(i)
