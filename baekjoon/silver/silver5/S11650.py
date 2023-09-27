# 5
# 3 4
# 1 1
# 1 -1
# 2 2
# 3 3

import sys
input = sys.stdin.readline

cnt = int(input())
nums = []
for _ in range(cnt):
    nums.append(list(map(int, input().split())))

nums.sort(key=lambda x: (x[0], x[1]))

for i in nums:
    print(i[0], i[1])