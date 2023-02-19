n,m = map(int, input().split())

min = 0

for i in range(m):
    list_tmp = list(map(int, input().split()))
    list_tmp.sort()
    if(min < list_tmp[0]):
        min = list_tmp[0]

print(min)


# 책 풀이
# min() 함수를 이용하는 답안
n,m = map(int, input().split())

result = 0

# 한줄씩 입력받아 확인
for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)

print (result)
