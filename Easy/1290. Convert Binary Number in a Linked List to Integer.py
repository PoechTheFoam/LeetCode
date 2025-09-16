# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        current=head
        length=0
        output=0
        i=1
        while current:
            length+=1
            current=current.next
        current=head
        for j in range(length):
            output+=current.val*2**(length-i)
            current=current.next
            i+=1
        return output
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
