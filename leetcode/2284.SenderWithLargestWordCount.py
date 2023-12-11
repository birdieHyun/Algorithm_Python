from typing import List
from collections import defaultdict
import heapq

class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:

        dicts = defaultdict(int)
        q = []

        for i in range(len(senders)):
            sender = senders[i]
            message = len(messages[i].split())
            dicts[sender] += message

        sender_set = set(senders)

        for i in sender_set:
            heapq.heappush(q, (dicts[i], i))


        return heapq.nlargest(1, q)[0][1]  # nlargest를 사용하여 가장 큰 요소 반환

s = Solution()
# messages = ["Hello userTwooo","Hi userThree","Wonderful day Alice","Nice day userThree"]
# senders = ["Alice","userTwo","userThree","Alice"]

# messages = ["How is leetcode for everyone","Leetcode is useful for practice"]
# senders = ["Bob","Charlie"]

messages = ["tP x M VC h lmD","D X XF w V","sh m Pgl","pN pa","C SL m G Pn v","K z UL B W ee","Yf yo n V U Za f np","j J sk f qr e v t","L Q cJ c J Z jp E","Be a aO","nI c Gb k Y C QS N","Yi Bts","gp No g s VR","py A S sNf","ZS H Bi De dj dsh","ep MA KI Q Ou"]
senders = ["OXlq","IFGaW","XQPeWJRszU","Gb","HArIr","Gb","FnZd","FnZd","HArIr","OXlq","IFGaW","XQPeWJRszU","EMoUs","Gb","EMoUs","EMoUs"]

print(s.largestWordCount(messages, senders))