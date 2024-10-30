class Solution:
    def merge_two(self, l1, l2):
        head = ListNode(0)
        cur = head
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        if l1 != None:
            cur.next = l1
        if l2 != None:
            cur.next = l2

        return head.next


    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        elif len(lists) == 1:
            return lists[0]
        elif len(lists) == 2:
            return self.merge_two(lists[0], lists[1])
        else:
            mid = len(lists) // 2
            l = self.mergeKLists(lists[:mid])
            r = self.mergeKLists(lists[mid:])

            return self.merge_two(l, r)
