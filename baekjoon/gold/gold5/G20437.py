from collections import defaultdict

test = int(input())

for _ in range(test):
    dict = []
    str = input()
    word_len = int(input())

    for i in str:
        if str.count(i) == word_len:
            dict[k]