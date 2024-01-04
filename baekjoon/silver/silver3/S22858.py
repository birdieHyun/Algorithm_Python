import sys

input = sys.stdin.readline

N, K = map(int, input().split())
after_shuffle = list(map(int, input().split()))
shuffle_index = list(map(int, input().split()))

for _ in range(K):
    tmp = [0] * (N + 1)

    for i in shuffle_index:
        tmp[shuffle_index.index(i) + 1] = after_shuffle[i - 1]

    after_shuffle = tmp

for i in after_shuffle:
    print(i, end=' ')
