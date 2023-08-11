from collections import deque


def lengthOfLongestSubstring(s: str) -> int:
    answer = 1
    for i in range(len(s)):
        tmp = s[i]

        q = deque(tmp)
        count = 0

        for j in range(i + 1, len(s)):
            next_s = s[j]

            if next_s in q:
                break

            count += 1
            q.append(next_s)

        if count > answer:
            answer = count

    return answer


print(lengthOfLongestSubstring('abcabcd'))
