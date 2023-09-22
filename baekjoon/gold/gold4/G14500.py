height, width = map(int, input().split())

tetro = []

for i in range(height):
    tetro.append(list(map(int, input().split())))
max_num = 0
def bfs1(tetro, x, y):
    tmp = 0



    return tmp


def bfs2(tetro, x, y):
    tmp = 0

    return tmp


def bfs3(tetro, x, y):
    tmp = 0

    return tmp


def bfs4(tetro, x, y):
    tmp = 0

    return tmp


def bfs5(tetro, x, y):
    tmp = 0

    return tmp

for i in range(height):
    for j in range(width):
        b1 = bfs1(tetro, j, i)
        b2 = bfs2(tetro, j, i)
        b3 = bfs3(tetro, j, i)
        b4 = bfs4(tetro, j, i)
        b5 = bfs5(tetro, j, i)
        max_num = max(max_num, b1, b2, b3, b4, b5)


