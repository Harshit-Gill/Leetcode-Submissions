class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        slow = 0
        for fast in range(0,len(nums)):
            if nums[fast] != 0:
                nums[slow] , nums[fast] = nums[fast], nums[slow]
                slow += 1       