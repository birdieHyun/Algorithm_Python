N, S, M = map(int, input().split())
lists = list(map(int, input().split()))
dp = [0] * N


def check_max(num1, num2):
    if num1 < 0 or num1 > M:
        if num2 < 0 or num2 > M:
            raise Exception
        else:
            return num2
    elif num2 < 0 or num2 > M:
        if num1 < 0 or num1 > M:
            raise Exception
        else:
            return num1
    else:
        return max(num1, num2)
try:
    dp[0] = check_max(S - lists[0], S + lists[0])


    print(dp[-1])
except:
    print(-1)