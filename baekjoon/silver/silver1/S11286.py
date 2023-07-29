import heapq, sys

input = sys.stdin.readline

arr = []

count = int(input())

for _ in range(count):
    num = int(input())
    tmp = (abs(num), num)

    if num == 0:
        if len(arr) > 0:
            print(heapq.heappop(arr)[1])
        else:
            print(0)

    if num != 0:
        heapq.heappush(arr, (abs(num), num))
