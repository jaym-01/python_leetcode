class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        i = 0
        cur = head

        while i < 10**4 + 1:
            if cur == None:
                return False
            else:
                cur = cur.next
            i += 1
        return True
