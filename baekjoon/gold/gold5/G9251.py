A = str(input().strip())
B = str(input().strip())

last_index = 0
a_answer = []
b_answer = []

for i in range(len(A)):
    for j in range(last_index, len(B)):
        if A[i] == B[j]:
            a_answer.append(B[j])
            last_index = j + 1
            break

last_index = 0
for i in range(len(B)):
    for j in range(last_index, len(A)):
        if B[i] == A[j]:
            b_answer.append(A[j])
            last_index = j + 1
            break

print(max(len(a_answer), len(b_answer)))