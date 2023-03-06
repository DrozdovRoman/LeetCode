class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        index = 0
        while( index < len(nums) and nums[index] != 0):
            index += 1
        j = index
        for i in range(index, len(nums)):
            if (nums[i] != 0):
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
