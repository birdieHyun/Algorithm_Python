num_len, test_case = map(int, input().split())

nums = list(map(int, input().split()))
check = [0]

for i in range(len(nums)):
    check.append(check[i] + nums[i])

for _ in range(test_case):
    from_num, to_num = map(int,input().split())

    print(check[to_num] - check[from_num - 1])
