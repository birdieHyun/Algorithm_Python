l, c = map(int, input().split())
words = sorted(list(map(str, input().split())))
vowels = ['a', 'e', 'i', 'o', 'u']
answer = []


def back_tracking(cnt, idx):
    if cnt == l:
        vowel, consonant = 0, 0

        for i in range(l):
            if answer[i] in vowels:
                vowel += 1
            else:
                consonant += 1

        if vowel >= 1 and consonant >= 2:
            print("".join(answer))
        return

    for i in range(idx, c):
        answer.append(words[i])
        back_tracking(cnt + 1, i + 1)
        answer.pop()


back_tracking(0, 0)
