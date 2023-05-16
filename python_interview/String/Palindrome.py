from collections import deque

input_str = input()

def isPalindrome(str_input):
    str_list = deque()
    for x in str_input:
        if x.isalnum():
            str_list.append(x)

    while len(str_list) > 1:
        if str_list.popleft() != str_list.pop():
            return False

    return True


print(isPalindrome(input_str))