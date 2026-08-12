class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq={}
        maxcnt=0
        i=0
        j=0
        while j<len(nums):
            freq[nums[j]]=freq.get(nums[j], 0) +1
            while freq[nums[j]]>k:
                freq[nums[i]]-=1
                i=i+1
            cnt=j-i+1
            maxcnt=max(maxcnt, cnt)
            j=j+1
        return maxcnt



            