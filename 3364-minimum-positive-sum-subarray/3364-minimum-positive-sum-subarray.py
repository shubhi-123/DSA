class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        mini=float('inf')
        for i in range(len(nums)):
            s=0
            for j in range(i,len(nums)):
                s+=nums[j]
                if l<=j-i+1<=r and s>0:
                    mini=min(mini,s)
        return mini if mini!=float('inf') else -1