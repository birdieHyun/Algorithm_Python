from collections import deque


def solution(cacheSize, cities):
    answer = 0
    cache = deque()
    if cacheSize == 0:
        return 5 * len(cities)

    for city in cities:
        # 캐시 사이즈보다 작은 경우 넣음
        city = city.lower()
        if len(cache) < cacheSize:
            # 캐시에 있다면 최산화 필요
            if city in cache:
                cache.remove(city)
                cache.append(city)
                answer += 1
            else:
                cache.append(city)
                answer += 5
        # 캐시 사이즈보다 크거나 같은 경우
        else:
            if city in cache:
                cache.remove(city)
                answer += 1
            else:
                answer += 5
                cache.popleft()

            cache.append(city)

    return answer


print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))

# 최대 도시의 수 100_00
# cache size = 30
# 캐시 히트 = 1 캐시 미스 = 5초
# cities 조회하면서 cache 조회하면서 중복되는거 제거 (contains and remove)

# 캐시 사이즈가 0인 고려 처음에 고려 x
# 대소문자 고려 x