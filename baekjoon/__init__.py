def min_fuel_required(time, power, distance):
    # 가속 구간에서 최대로 도달할 수 있는 거리 계산
    low, high = 0, time
    while low < high:
        mid = (low + high) // 2
        acc_distance = power * mid * mid / 2
        if acc_distance >= distance:
            high = mid
        else:
            low = mid + 1

    # 가속 구간이 전체 거리를 커버하는지 확인
    if power * low * low / 2 >= distance:
        return low

    # 등속 구간 시간 계산
    constant_speed_time = (distance - power * low * low / 2) / (power * low)
    if low + constant_speed_time <= time:
        return low
    else:
        return -1  # 시간 내에 도착 불가능

def solution(total_fuel, powers, distances):
    # 가능한 최소 시간과 최대 시간 설정
    low, high = 1, max(distances) // min(powers) * 2

    while low < high:
        mid = (low + high) // 2
        fuel_used = 0

        # 각 우주선에 대한 연료 계산
        for i in range(len(powers)):
            fuel = min_fuel_required(mid, powers[i], distances[i])
            if fuel == -1:
                fuel_used = total_fuel + 1  # 불가능한 경우
                break
            fuel_used += fuel

        # 연료 사용량 확인
        if fuel_used <= total_fuel:
            high = mid
        else:
            low = mid + 1

    return low

fuel = 5
powers = [1, 2, 3, 4, 5]
distances = [50, 40, 30, 20, 10]

print(solution(fuel, powers, distances))
