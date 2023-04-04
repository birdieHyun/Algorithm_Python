def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    for i in range(0, len(A)):
        answer += A[i] * B[len(B) - i - 1]
    return answer

a = [1, 4, 2]
b = [5, 4, 4]

print(solution(a,b))

