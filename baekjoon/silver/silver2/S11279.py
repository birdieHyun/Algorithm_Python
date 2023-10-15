import heapq
import sys

input = sys.stdin.readline

N = int(input())

q = []
count = 0
for _ in range(N):
    tmp = int(input())

    if tmp != 0:
        heapq.heappush(q, -tmp)
    else:
        if len(q) > 0:
            print(-heapq.heappop(q))
        else:
            print(0)

