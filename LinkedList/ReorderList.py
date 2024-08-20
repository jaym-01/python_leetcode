def reorderList(self, head: Optional[ListNode]) -> None:   
    """
    Do not return anything, modify head in-place instead.
    """
    self.helper(head, head)
    

def helper(self, head: Optional[ListNode], end: Optional[ListNode]) -> Optional[ListNode] | int:
    if end == None:
        return None
    
    res = self.helper(head, end.next)
    
    if res != None:
        cur = res
    elif res == -1:
        return -1
    elif res == end:
        end.next = None
        return -1
    else:
        cur = head
    
    if cur.next == end:
        end.next = None
    else:
        end.next = cur.next
    out = cur.next
    cur.next = end
    
    return out