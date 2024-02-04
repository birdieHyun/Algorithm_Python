from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicts = defaultdict(list)

        for i in strs:
            s = ''.join(sorted(i))
            dicts[s].append(i)

        answer = list(dicts.values())
        answer.sort(key=lambda x : len(x))

        return answer

s = Solution()
anagrams = s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])

print(anagrams)
