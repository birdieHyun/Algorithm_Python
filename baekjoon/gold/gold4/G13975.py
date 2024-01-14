import sys
import heapq

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    count = int(input())
    pages = list(map(int, input().split()))
    answer = 0
    q = []

    for pages in pages:
        heapq.heappush(q, pages)

    while len(q) >= 2:
        result = 0
        first = heapq.heappop(q)
        second = heapq.heappop(q)

        result += (first + second)
        answer += result

        if not q:
            break

        heapq.heappush(q, result)

    print(answer)
