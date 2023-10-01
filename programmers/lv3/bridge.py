import heapq

def solution(stones, k):
    answer = []

    for i in range(len(stones) - k + 1): # O(N) 20만 - K
        tmp =[]
        for j in range(i, i+k):
            tmp.append(stones[j])
        heapq.heappush(answer, max(tmp))

    return heapq.heappop(answer)

stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3

print(solution(stones, k))
