"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if (root == None):
            return root
        first = root
        while first.left != None:
            parent = first
            while parent != None:
                parent.left.next = parent.right
                if parent.next != None:
                    parent.right.next = parent.next.left
                parent = parent.next
            first = first.left

        return root