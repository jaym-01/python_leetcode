from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # recursive solution
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     if head == None:
    #         return None
    #     else:
    #         return self.helper(head, None) 
    
    # def helper(self, head, next):
    #     tmp = head.next
    #     head.next = next
    #     if tmp == None:
    #         return head
    #     else:
    #         return self.helper(tmp, head)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:        
        curr = head
        nxt = None

        while(curr != None):
            tmp = curr.next
            curr.next = nxt
            nxt = curr
            curr = tmp

        return nxt



# DEBUGGING
def createList(x):
    head = ListNode(x[0])
    curr = head

    for i in range(1, len(x)):
        curr.next = ListNode(x[i])
        curr = curr.next
    
    curr.next = None
    return head

def printList(x):
    if x == None:
        print("\n", end="")
        return
    else:
        print(f"{x.val}", end=", ")
        return printList(x.next)

if __name__ == "__main__":
    test = Solution()
    tmp = createList([1,2,3,4,5])
    printList(test.reverseList(tmp))