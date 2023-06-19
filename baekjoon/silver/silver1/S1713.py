from collections import deque

frame_size = int(input())
suggestion_count = int(input())
suggest_list = list(map(int, input().split()))

total_student = max(suggest_list) + 1
photo_frame = deque()
students = [[i, 0] for i in range(total_student)]

for i in range(suggestion_count):
    suggested = suggest_list[i]
    students[suggested][1] += 1

    print(photo_frame)
    photo_frame = deque(sorted(photo_frame, key=lambda x: [1]))

    if len(photo_frame) == frame_size:
        for i in range(len(photo_frame)):
            if photo_frame[i] <= photo_frame[i + 1]:
                print(photo_frame.popleft())
                break
    if students[suggested] not in photo_frame:
        photo_frame.append(students[suggested])


print(photo_frame)