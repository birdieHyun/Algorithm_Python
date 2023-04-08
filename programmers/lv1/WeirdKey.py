import numpy as np
def solution(keymap, targets):
    answer = []

    for target in targets:
        tmp_num = 0
        for t in target:
            num_lst = []
            for k in keymap:
                try:
                    num_lst.append(k.index(t))
                except:
                    num_lst.append(np.inf)

            tmp_num += (min(num_lst) + 1)

        if tmp_num == np.inf:
            answer.append(-1)
        else:
            answer.append(tmp_num)

    answer

    return answer
