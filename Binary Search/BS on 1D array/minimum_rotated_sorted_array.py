class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        high=n-1
        low=0
        while (low<high):
            mid=(low+high)//2
            if nums[mid]>nums[high]:
                low=mid+1
            else:
                high=mid
        return nums[low]