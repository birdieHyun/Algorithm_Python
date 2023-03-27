def solution(wallpaper):
    answer = []
    row = []
    column = []

    for i in range(len(wallpaper)):
        first = int(wallpaper[i].find("#"))
        last = int(wallpaper[i].rfind("#"))
        if first != -1:
            row.append(first)
        if last != -1:
            row.append(last)
        if first != -1 or last != -1:
            column.append(i)

    row.sort()
    column.sort()

    answer.append(column[0])
    answer.append(row[0])
    answer.append(column[-1] + 1)
    answer.append(row[-1] + 1)

    return answer


wallpaper = ["..........", ".....#....", "......##..", "...##.....", "....#....."]
print(solution(wallpaper))
