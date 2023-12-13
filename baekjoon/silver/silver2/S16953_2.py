# 10^9 인것을 보고 O(n^2) 이면 안되겠다 생각되어 dp 생각
# 그러나 공간복잡도를 고려하지 않아서 메모리 초과 발생

# start, target = map(int, input().split())
#
# dp = [int(10e9)] * (target + 1)
# dp[start] = 1
#
# for i in range(start, target + 1):
#     first = i * 2
#     second = int(str(i) + '1')
#     if first <= target:
#         dp[first] = min(dp[i] + 1, dp[first])
#     if second <= target:
#         dp[second] = min(dp[i] + 1, dp[second])
#
# if dp[target] == int(10e9):
#     print(-1)
# else:
#     print(dp[target])

########################3

from collections import deque

start, target = map(int, input().split())

q = deque()
q.append((start, 1))
flag = False

while q:

    now, count = q.popleft()

    if now > target:
        continue
    if now == target:
        print(count)
        flag = True
        break

    q.append((now * 2, count + 1))
    q.append((int(str(now) + '1'), count + 1))

if not flag:
    print(-1)
