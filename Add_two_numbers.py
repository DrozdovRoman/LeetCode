# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        r1 = 0
        r2 = 0
        count = 1
        while (l1 != None):
            r1 += l1.val * count
            count *= 10
            l1 = l1.next
        count = 1
        while (l2 != None):
            r2 += l2.val * count
            count *= 10
            l2 = l2.next
        x = r1 + r2
        result = ListNode()
        current = result
        while (x != 0):
            current.val = x % 10
            current.next = ListNode()
            current = current.next
            x = x / 10
        return(result)