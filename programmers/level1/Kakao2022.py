def solution(id_list, report, k):
    answer = []
    reported = []
    id_dic = {}

    for i in range(len(id_list)):
        id_dic[id_list[i]] = 0

    for i in range(len(report)):
        list = report[i].split(" ")
        if report[i] not in reported:
            reported.append(report[i])
            id_dic[list[1]] += 1

    for i in range(len(id_list)):
        if id_dic[id_list[i]] >= k:
            answer.append(id_dic[id_list[i]] + 1 - k)
        else:
            answer.append(0)

    return answer


id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
k = 2

# id_list = ["con", "ryan"]
# report = ["ryan con", "ryan con", "ryan con", "ryan con"]
# k = 3

print(solution(id_list, report, k))
