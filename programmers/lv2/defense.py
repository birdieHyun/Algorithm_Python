import heapq

def solution(n, k, enemy):
    answer = 0

    round_list = []

    for i in range(len(enemy)):
        n -= enemy[i]
        heapq.heappush(round_list, -enemy[i])
        while n < 0 and k > 0:
            k -= 1
            n += -heapq.heappop(round_list)

        if k == 0 and n <= 0:
            if n == 0:
                answer = i + 1
            elif n < 0:
                answer = i
            return answer

    return len(enemy)


n = 7
k = 3
enemy = [4, 2, 4, 5, 3, 3, 1]

print(solution(n,k,enemy))