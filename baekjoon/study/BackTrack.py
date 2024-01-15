alpha = ['A', 'B', 'C', 'D']
used = [False] * 4

def backtrack(string):

    if len(string) == 4:
        print(string)
        return

    for i in range(len(alpha)):
        if not used[i]:
            used[i] = True
            backtrack(string + alpha[i])
            used[i] = False


backtrack('')