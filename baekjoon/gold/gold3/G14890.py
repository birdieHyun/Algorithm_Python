n, l = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
answer = 0


def slope(node):
    for j in range(1, n):
        if abs(node[j] - node[j - 1]) > 1:
            return False
        if node[j] < node[j - 1]:
            for k in range(l):
                if j + k >= n or used[j + k] or node[j] != node[j + k]:
                    return False
                if node[j] == node[j + k]:
                    used[j + k] = True
        elif node[j] > node[j - 1]:
            for k in range(l):
                if j - k - 1 < 0 or node[j - 1] != node[j - k - 1] or used[j - k - 1]:
                    return False
                if node[j - 1] == node[j - k - 1]:
                    used[j - k - 1] = True
    return True


for i in range(n):
    used = [False for _ in range(n)]
    if slope(maps[i]):
        answer += 1

for i in range(n):
    used = [False for _ in range(n)]
    if slope([maps[j][i] for j in range(n)]):
        answer += 1

print(answer)
