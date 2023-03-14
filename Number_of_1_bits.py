# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         return n.bit_count()

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            count += 1
            n &= (n - 1)
        return count
