# def solution(park, routes):
#     answer = []
#     start = findStart(park)
#
#     for i in range(len(routes)):
#         move_coordinate = moving(routes)
#         if can_move(park, move_coordinate, start):
#
#
#     return answer
#
#
# def can_move(park, moving, current_location):
#     for i in range(1, moving[1] + 1):
#         if moving[0] == 'E':
#             if park[current_location[0] + i][current_location[1]] == 'X':
#                 return False
#
#         if moving[0] == 'W':
#             if park[current_location[0] - i][current_location[1]] == 'X':
#                 return False
#
#         if moving[0] == 'S':
#             if park[current_location[0]][current_location[1] - i] == 'X':
#                 return False
#         if moving[0] == 'N':
#             if park[current_location[0]][current_location[1] + i] == 'X':
#                 return False
#     return [0,0]
#
#
#
# # 어디로 얼만큼 갈지 결정
# def moving(location):
#     move = location.split()
#     coordinate = move[0]
#     index = int(move[1])
#
#     if coordinate == 'E':
#         return [index, 0]
#     elif coordinate == 'W':
#         return [-index, 0]
#     elif coordinate == 'N':
#         return [0, index]
#     elif coordinate == 'S':
#         return [0, -index]
#
#
# # 시작점 찾기
# def findStart(location):
#     for i in range(len(location)):
#         for j in range(len(location[i])):
#             if location[i][j] == 'S':
#                 return [j, i]
#
#
# park = ["SOO", "OOO", "OOO"]
# routes = ["E 2", "S 2", "W 1"]
#
# print(solution(park, routes))
