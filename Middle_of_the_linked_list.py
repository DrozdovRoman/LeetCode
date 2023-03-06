# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fastPoint = head
        slowPoint = head
        while(fastPoint != None and fastPoint.next != None):
            slowPoint = slowPoint.next
            fastPoint = fastPoint.next.next
        return slowPoint