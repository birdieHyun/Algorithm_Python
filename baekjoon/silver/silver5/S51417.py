number_of_candidate = int(input())

candidate = []
answer = 0
my = int(input())

for i in range(number_of_candidate -1):

    candidate.append(int(input()))

candidate.sort(reverse=True)

if number_of_candidate == 1:
    print(0)
else:
    while candidate[0] >= my:
        candidate[0] -= 1
        my += 1
        answer += 1
        candidate.sort(reverse=True)

    print(answer)
