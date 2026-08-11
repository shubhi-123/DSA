class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        finalsum = nums[0]
        i = 0
        while i + 1 < len(nums) and nums[i + 1] == nums[i] + 1:
            i += 1
            finalsum += nums[i]
        while finalsum in nums:
            finalsum += 1
        return finalsum

