from math import ceil


def solution(fees, records):
    answer = []
    default_time, default_fee, unit_time, unit_fee = fees
    parking = {}
    using_time = {}

    for record in records:
        time, number, io = record.split()
        hour, minute = map(int, time.split(":"))
        time = hour * 60 + minute
        if io == "IN":
            parking[number] = time
        elif io == "OUT":
            if number in using_time:
                using_time[number] += (time - parking[number])
            else:
                using_time[number] = time - parking[number]
            del parking[number]

    for number, time in parking.items():
        if number in using_time:
            using_time[number] += 1439 - time
        else:
            using_time[number] = 1439 - time

    for number, time in sorted(using_time.items(), key=lambda x: x[0]):
        answer.append(default_fee + max(0, ceil((time - default_time) / unit_time)) * unit_fee)

    return answer

# fees [0] = 기본 시간
# fees [1] = 기본 요금
# fees [2] = 단위 시간
# fees [3] = 단위 요금

# ["05:34 5961 IN"] 공백 기준으로 시각 차량번호 출입 관리

# 입차 후 출차 내역이 없으면 23:59에 출차된 것으로 간주한다.

# 차량 번호 작은 자동차부터 요금 계산

# 같은 차량이 입차 출차를 두 번 하는 경우는? -> out 할 떄 remove 처리해주기

# 1. 차량 번호를 key 로 IN 이면 dict에 input / OUT 이면 시각 계산 후 dict 에서 remove
# 2. 시간 계산 후 기본 시각에 포함되는지 확인
# 2 - 1 기본 시각에 포함된다면 기본요금만, 초과된다면 요금 계산
# 2 - 2 출차가 안된게 있다면 23:59 출차 처리
# 3 - 요금 dict 에 저장하기
