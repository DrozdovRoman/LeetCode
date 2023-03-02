class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [None for i in range(len(nums))]
        first, last = 0, len(nums) - 1
        for i in range(len(nums)-1,-1,-1):
            if abs(nums[first]) > nums[last]:
                result[i] = nums[first] ** 2
                first += 1
                continue
            result[i] = nums[last] ** 2
            last -= 1
        return result
