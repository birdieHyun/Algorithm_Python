def solution(m, n, board):
    answer = 0
    board = list(map(list, board))

    tmp = set()
    while True:

        for i in range(m - 1):
            for j in range(n - 1):
                t = board[i][j]
                if t == []: # 비어있다면
                    continue
                else:
                    if board[i][j + 1] == t and board[i + 1][j] == t and board[i + 1][j + 1] == t:
                        tmp.add((i, j))
                        tmp.add((i, j + 1))
                        tmp.add((i + 1, j))
                        tmp.add((i + 1, j + 1))
        if tmp:
            answer += len(tmp)
            for i, j in tmp:
                board[i][j] = []
            tmp = set()
        else:
            break

        while True:
            moved = 0
            for i in range(m - 1):
                for j in range(n):
                    if board[i][j] and board[i + 1][j] == []:
                        board [i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
                        moved = 1
            if moved == 0:
                break

    return answer

# m = 높이 , n = 폭, board = 배치정보
# 라이언(R), 무지(M), 어피치(A), 프로도(F), 네오(N), 튜브(T), 제이지(J), 콘(C)

# 2 X 2 가 되어야 지워짐
# 지금 블록을 기준으로 하나 아래, 하나 오른쪽, 하나 오른대각아래 같은 블록인지 확인
# 같은 블록이라면 queue 에 삽입
# count += 1

# 한 싸이클 돌면 각 요소들 전부 아래로 내려야 함