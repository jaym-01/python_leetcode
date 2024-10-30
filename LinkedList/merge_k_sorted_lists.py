class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        i = -2
        cur = None
        head = None

        while i != -1:
            i = -1
            smallest = None
            for j, l in enumerate(lists):
                if l != None and (smallest == None or smallest.val > l.val):
                    i = j
                    smallest = l
            
            if head == None:
                head = smallest
                cur = head
            else:
                cur.next = smallest
                cur = cur.next

            if i > -1:
                lists[i] = lists[i].next

        return head
