#n 개의 총 길이, m 이 롤러의 길이, section[] 이 칠해야 할 구역

def solution(n, m, section):
    count = 0
    while section:
        end = section[-1] - 1
        start = end -m + 1

        if start < 0:
            start, end = 0, m -1
        count += 1

        while start <= section[-1] - 1:
            section.pop()
            if not section:
                break

    return count


