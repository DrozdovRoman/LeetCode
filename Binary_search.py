class Solution:
    def search(self, nums: List[int], target: int) -> int:
        leftSide, rightSide = 0, len(nums) - 1
        while (leftSide <= rightSide):
            k = (leftSide + rightSide) // 2
            if nums[k] == target:
                return k
            elif nums[k] > target:
                rightSide = k - 1
            elif nums[k] < target:
                leftSide = k + 1
        return -1