n, w, l = map(int, input().split())
trucks = list(map(int, input().split()))

bridge = [0] * w
time = 0

while bridge:
    bridge.pop(0)
    time += 1
    if trucks:
        if sum(bridge) + trucks[0] <= l:
            bridge.append(trucks.pop(0))

        else:
            bridge.append(0)

print(time)
