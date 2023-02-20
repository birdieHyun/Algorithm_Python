index = input()

indexX = int(ord(index[0]) - int(ord('a')) + 1)
indexY = int(index[1])
answer = 0

move = [[-2, -1], [-2, 1], [2, -1], [2, 1], [1, 2], [1, -2], [-1, 2], [-1, -2]]

for i in move:
    nextX = indexX + i[0]
    nextY = indexY + i[1]
    if nextX<= 8 and nextX >= 1 and nextY <=8 and nextY >= 1:
        answer += 1
print(answer)