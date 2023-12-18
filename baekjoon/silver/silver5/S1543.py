origin = str(input())
target = str(input())

t_len = len(target)
answer = 0

i = 0
while i < len(origin) - t_len + 1:
    now = origin[i : i + t_len]

    if now == target:
        i += t_len
        answer += 1
        continue
    i += 1

print(answer)