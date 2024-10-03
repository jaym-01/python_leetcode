class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = None
        cur = None

        def process_sum(val: int):
            nonlocal cur, carry

            if cur is None:
                cur = ListNode(val % 10)
            else:
                cur.next = ListNode(val % 10)
                cur = cur.next

            if val > 9:
                carry = 1
            else:
                carry = 0

        while l1 != None or l2 != None: 
            if l1 == None:
                process_sum(l2.val + carry)
                l2 = l2.next
            elif l2 == None:
                process_sum(l1.val + carry)
                l1 = l1.next
            else:
                process_sum(l1.val + l2.val + carry)
                l1 = l1.next
                l2 = l2.next

            if head is None:
                head = cur

        if carry > 0:
            cur.next = ListNode(carry)
        
        return head
