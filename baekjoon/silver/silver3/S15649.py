import sys

input = sys.stdin.readline

N, M = map(int, input().split())

used = [False] * (N + 1)


def backtrack(cnt, s):
    if cnt == M:
        print(s.strip())

    for i in range(1, N + 1):
        if not used[i]:
            used[i] = True
            backtrack(cnt + 1, s + " " + str(i))
            used[i] = False


backtrack(0, "")
