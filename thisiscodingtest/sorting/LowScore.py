people = int(input())

people_list = []
for _ in range(people):
    print(1)
    person, score = map(str, input().split())

    people_list.append((person, int(score)))

    list = sorted(people_list, key=lambda x: x[1], reverse=True)

for i in list:
       print(i[0], end=' ')