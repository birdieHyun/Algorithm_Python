from typing import List, Optional
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        q = []

        # 각 연결 리스트의 노드를 힙에 추가
        for node in lists:
            while node:
                heapq.heappush(q, node.val)
                node = node.next

        # 더미 노드 생성
        dummy = ListNode(0)
        current = dummy

        # 힙에서 요소를 꺼내어 새 연결 리스트 생성
        while q:
            val = heapq.heappop(q)
            current.next = ListNode(val)
            current = current.next

        return dummy.next


s = Solution()

lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
print(s.mergeKLists(lists))
