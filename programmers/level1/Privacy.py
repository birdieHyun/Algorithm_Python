def solution(today, terms, privacies):
    answer = []
    max_expire = get_total_date(today)
    my_dic = {}
    for i in range(len(terms)):
        split = terms[i].split()
        my_dic[split[0]] = (int(split[1]) * 28)

    for i in range(len(privacies)):
        tmp_list = privacies[i].split()

        privacy = get_total_date(tmp_list[0]) + my_dic[tmp_list[1]]

        if privacy <= max_expire:
            answer.append(i + 1)

    return answer

def get_total_date(date):
    year, month, day, = map(int, date.split("."))
    return (year * 12 * 28) + month * 28 + day


today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]

print(solution(today, terms, privacies))

today2 = "2020.01.01"
term2 = ["Z 3", "D 5"]
privacies2 = ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]

print(solution(today2, term2, privacies2))
