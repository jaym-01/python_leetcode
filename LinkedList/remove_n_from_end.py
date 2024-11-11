class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def solution(cur, n):
            if cur == None:
                return n, cur
            else:
                m, head = solution(cur.next, n)
                if m == 1:
                    return m - 1, head
                else:
                    cur.next = head
                    return m - 1, cur
        return solution(head, n)[1]
