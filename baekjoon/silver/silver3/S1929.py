import math

def prime(x):
    for i in range(2, int(math.sqrt(x) + 1)):
        if x % i == 0:
            return False
    print(x)
    return True

start, finish = map(int, input().split())

for i in range(start, finish + 1):
    prime(i)

