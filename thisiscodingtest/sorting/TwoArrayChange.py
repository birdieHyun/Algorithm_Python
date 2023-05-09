size, count = map(int, input().split())

first = list(map(int, input().split()))

second = list(map(int, input().split()))

first.sort()
second.sort(reverse=True)

for i in range(count):
    if first[i] >= second[i]:
        first[i], second[i] = second[i], first[i]
    else:
        break

print(sum(first))

