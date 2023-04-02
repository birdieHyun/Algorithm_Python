from collections import defaultdict

def solution(survey, choices):
    # 미리 값을 0으로 설정
    score_dic = defaultdict(int)

    # survey 조회하며 점수 더하기
    for i in range(len(survey)):
        one_survey = list(survey[i])
        user_choice = choices[i]

        # 0점일 경우 무시하기
        if user_choice == 4:
            continue

        # 불만족 점수 더하기
        elif user_choice > 0 and user_choice < 4:
            tmp = one_survey[0]
            score_dic[tmp] += getScore(user_choice)

        # 만족 점수 더하기
        elif user_choice > 4 and user_choice < 8:
            tmp = one_survey[1]
            score_dic[tmp] += getScore(user_choice)

    first = find_one_mbti('R', 'T', score_dic)
    second = find_one_mbti('C', 'F', score_dic)
    third = find_one_mbti('J', 'M', score_dic)
    fourth = find_one_mbti('A', 'N', score_dic)

    return first + second + third + fourth

# 만족 불만족에 따른 점수 부여
def getScore(number):
    if number == 1:
        return 3
    elif number == 2:
        return 2
    elif number == 3:
        return 1
    elif number == 4:
        return 0
    elif number == 5:
        return 1
    elif number == 6:
        return 2
    elif number == 7:
        return 3

# mbti 하나 결정하기, 점수가 같으면 앞선 mbti 부여
def find_one_mbti(a, b, score_dict):
    if score_dict[a] > score_dict[b]:
        return a
    elif score_dict[a] < score_dict[b]:
        return b
    else:
        return a


survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]
print(solution(survey, choices))

survey2 = ["TR", "RT", "TR"]
choices2 = [7, 1, 3]
print(solution(survey2, choices2))

# R 라이언형 , T 튜브형
# C 콘형 , F 프로도형
# J 제이지형, M 무지형
# A 어피치형, N 네오형

# 1	매우 비동의    - 3점
# 2	비동의        - 2점
# 3	약간 비동의    - 1점
# 4	모르겠음      - 0점
# 5	약간 동의     - 1점
# 6	동의         - 2점
# 7	매우 동의     - 3점

