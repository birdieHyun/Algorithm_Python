from collections import Counter


def solution(str1, str2):
    str1_low = str1.lower()
    str2_low = str2.lower()

    st1_list = []
    st2_list = []

    for i in range(len(str1_low) - 1):
        if str1_low[i].isalpha() and str1_low[i + 1].isalpha():
            st1_list.append(str1_low[i] + str1_low[i + 1])

    for i in range(len(str2_low) - 1):
        if str2_low[i].isalpha() and str2_low[i + 1].isalpha():
            st2_list.append(str2_low[i] + str2_low[i + 1])

    counter1 = Counter(st1_list)
    counter2 = Counter(st2_list)

    inter = list((counter1 & counter2).elements())
    union = list((counter1 | counter2).elements())

    if len(union) == 0 and len(inter) == 0:
        return 65536

    return int(len(inter) / len(union) * 65536)


print(solution('FRANCE', 'french'))

# 입력받은 문자 영문자로만 isAlpha 로 두글자씩 끊어서 확인
# 소문자로
# 0 ~ 1사이의 실수 구한 후 65536 곱하고 정수부만 출력
# 둘 다 변환 후가 비어있으면 65536 이 정답
# 둘 중 하나만 비어있으면 0 정답

# 그냥 set() 을 하게 되면 [aa aa aa] 이렇게 있는 리스트의 자카드 구할 수 없음
# Counter 객체는 전처리된 리스트 형태의 st1_list 와 st2_list 를 각각 Counter 객체로 변환해준다. (각 요소가 몇개인지 key val 로 표현)
