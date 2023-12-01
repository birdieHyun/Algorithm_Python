import sys
input = sys.stdin.readline


N = int(input())
K = int(input())
node = list(map(int, input().split()))
node.sort()

# 센서와 집중국의 개수가 같은 경우
if K >= N:
    print(0)
    sys.exit()

# 센서들 간의 거리 측정
dist = []

for i in range(len(node) - 1):
    dist.append(node[i + 1] - node[i])

dist.sort(reverse=True)

for _ in range(K-1):
    dist.pop(0)

print(sum(dist))
