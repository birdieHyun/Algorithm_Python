from collections import deque

collect_size = int(input())
students = int(input())
std_list = list(map(int, input().split()))

collect = deque()

for i in range(students):
    std = std_list[i]

    if any(student[0] == std for student in collect):
        tmp = [student[0] for student in collect].index(std)
        collect[tmp][1] += 1       # 추천 수 더해준다.

        while tmp < collect_size - 1: # tmp 를 전체 사이즈 순회하면서 적절한 위치로 옮겨준다.
            if collect[tmp][1] >= collect[tmp + 1][1]:       # 추천수가 같거나 크다면 위치를 바꿔준다.
                collect[tmp], collect[tmp + 1] = collect[tmp + 1], collect[tmp]
            tmp += 1

    # collect 에 없을 경우
    else:
        collect.append([std, 1])

        # 사이즈 비교를 해준다.
        if len(collect) > collect_size:
            collect.popleft()

            tmp = [student[0] for student in collect].index(std)

            while tmp > 0:
                if collect[tmp][1] < collect[tmp - 1][1]:
                    collect[tmp][1], collect[tmp - 1][1] = collect[tmp - 1][1], collect[tmp][1]
                tmp -= 1

answer = sorted(collect, key = lambda x : x[0])

for i in range(len(answer)):
    print(answer[i][0], end=' ')