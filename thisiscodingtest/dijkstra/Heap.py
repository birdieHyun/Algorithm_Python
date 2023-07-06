import heapq


def heapsort(iterable):
    h = []
    result = []

    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)

    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result


result = heapsort([1, 3, 4, 7, 9, 2, 4, 6, 8, 0])
print(result)


## 최대 힙을 구현하고 싶다면?
def maxheapsort(iterable):
    h = []
    result = []

    for value in iterable:
        heapq.heappush(h, -value)

    for i in range(len(h)):
        result.append(-heapq.heappop(h))

    return result


answer = maxheapsort([1, 3, 4, 7, 9, 2, 4, 6, 8, 0])
print(answer)
