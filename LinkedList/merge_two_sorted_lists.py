class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        out = None
        while list1 != None and list2 != None:
            if list1.val > list2.val:
                out = list1

