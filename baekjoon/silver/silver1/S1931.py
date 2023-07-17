meetings = int(input())

meet_list = [list(map(int, input().split())) for _ in range(meetings)]

meet_list.sort(key=lambda x : (x[1], x[0],))

answer, last = 0, 0

for start, finish in meet_list:
    if start >= last:
        answer += 1
        last = finish

print(answer)