def solution(board, moves):
    stacklist = []
    answer = 0

    for move in moves:
        for i in range(len(board)):
            if board[i][move - 1] != 0:
                stacklist.append(board[i][move - 1])
                board[i][move - 1] = 0

                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        answer += 2
                break
    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]


print(solution(board, moves))