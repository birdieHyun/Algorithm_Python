import sys
input = sys.stdin.readline

m, n = map(int, input().split())
nums = list(map(int, input().split()))
prefix_sum = [0]

tmp = 0
for i in nums:
    tmp += i
    prefix_sum.append(tmp)

for i in range(n):
    a, b = map(int, input().split())
    print(prefix_sum[b] - prefix_sum[a - 1])
