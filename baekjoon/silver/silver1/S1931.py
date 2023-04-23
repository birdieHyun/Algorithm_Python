from collections import *

meeting = deque()

meeting_count = int(input())

meeting_list = [list(map(int, input().split())) for _ in range(meeting_count)]

# [[0, 6], [1, 4], [2, 13], [3, 5], [3, 8], [5, 7], [5, 9], [6, 10], [8, 11], [8, 12], [12, 14]]
sorted_meeting = sorted(meeting_list, key=lambda x: x[0])
print(sorted_meeting)

meeting.append(sorted_meeting[0])

for i in range(1, len(sorted_meeting)):
    index = len(meeting) - 1

    if meeting[index][1] <= sorted_meeting[i][0]:
        meeting.append(sorted_meeting[i])

    print(i, meeting)
    first_start = meeting[index][0]
    last_start = meeting[index][1]

    queue_range = last_start - first_start
    print(queue_range)
