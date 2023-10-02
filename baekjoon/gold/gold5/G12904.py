S = str(input())
T = str(input())

for _ in range(len(T) - len(S)):
    if T[-1] == 'A':
        T = T[0:-1]
    else:
        T = T[0:-1]
        T = T[::-1]

if S == T:
    print(1)
else:
    print(0)

