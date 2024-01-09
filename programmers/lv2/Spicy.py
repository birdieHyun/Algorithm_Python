import heapq

def solution(scoville, K):
    answer = 0
    q = []

    # O(N)
    for i in scoville:
        heapq.heappush(q, i)

    while q:

        smallest = heapq.heappop(q)

        if smallest >= K:
            break
        elif smallest < K and not q:
            answer = - 1
            break
        else:
            if not q:
                break

            second = heapq.heappop(q)

            heapq.heappush(q, smallest + (second * 2))
            answer += 1

    return answer