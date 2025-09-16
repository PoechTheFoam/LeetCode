class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        output=ListNode(0,None)
        current=output
        while list1 is not None or list2 is not None:
            if list1.val<=list2.val:
                current.val=list1.val
                list1=list1.next
            elif list2.val<=list1.val:
                current.val=list2.val
                list2=list2.next
            output=output.next
        return output
list1=ListNode(1,ListNode(2,ListNode(4)))
list2=ListNode(1,ListNode(3,ListNode(4)))
solution=Solution()
print(solution.mergeTwoLists(list1,list2))