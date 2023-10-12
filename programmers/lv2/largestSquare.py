def solution(board):
    answer = 0

    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] > 0:
                board[i][j] += min(board[i - 1][j], board[i - 1][j - 1], board[i][j - 1])

    for i in range(len(board)):
        for j in range(len(board[0])):
            answer = max(answer, board[i][j])

    return answer * answer

# board[i][j] 가 오른쪽 아래에 있다고 가정하고 문제 풀기