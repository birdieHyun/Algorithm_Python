from collections import deque


# 다리에 올라간 무게가 weight 보다 작아야 함  -> sum(bridge) < weight
# popleft() 로 꺼내기

# 들어간 타임을 계산한 q도 생성

def solution(bridge_length, weight, truck_weights):
    answer = 0

    q = deque(truck_weights)
    bridge = deque()
    time = deque()

    while q:
        answer += 1


        # 시간이 지났다면 꺼내기
        if time:
            if answer - time[0] == bridge_length:
                bridge.popleft()
                time.popleft()


        # 무게가 적다면 넣기
        if sum(bridge) + q[0] <= weight:
            bridge.append(q.popleft())
            time.append(answer)

    return answer + bridge_length


bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]
answer = 8

print(solution(bridge_length, weight, truck_weights))