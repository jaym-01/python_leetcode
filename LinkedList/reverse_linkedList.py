class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# recursive
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    return self.helper(None, head)
    
def helper(self, prev: Optional[ListNode], cur: Optional[ListNode]) -> Optional[ListNode]:
    if cur == None:
        return None
    
    head = self.helper(cur, cur.next)
    
    cur.next = prev
    
    if head == None: return cur
    else: return head
    

# iterative
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None: return None

        cur = head.next
        head.next = None
        prev = head

        while cur != None:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        
        return prev