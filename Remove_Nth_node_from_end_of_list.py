# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fastPoint = head
        slowPoint = head
        for i in range(n):
            fastPoint = fastPoint.next
        while(fastPoint != None and fastPoint.next != None):
            fastPoint = fastPoint.next
            slowPoint = slowPoint.next
        if fastPoint == None:
            return slowPoint.next
        slowPoint.next = slowPoint.next.next
        return(head)
