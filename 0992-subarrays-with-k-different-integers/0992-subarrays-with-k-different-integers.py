class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        # BRUTE FORCE TLE 
        # cnt=0
        # for i in range(len(nums)):
        #     for j in range(i, len(nums)):
        #         if len(set(nums[i:j+1]))==k:
        #             cnt=cnt+1
        # return cnt

        #BETTER TLE 
        # i=0
        # j=0
        # cnt=0
        # while j<len(nums):
        #     while (len(set(nums[i:j+1])))<k and j<len(nums):
        #         j=j+1
        #     while (len(set(nums[i:j+1])))>k and i<=j:
        #         i=i+1
        #     temp=i
        #     while temp<=j and len(set(nums[temp:j+1]))==k:
        #         cnt=cnt+1
        #         temp=temp+1
        #     j=j+1
        # return cnt
        
        def atmost(k):
            freq={}
            left=0
            cnt=0
            for right in range(len(nums)):
                freq[nums[right]]=freq.get(nums[right], 0)+1
                while len(freq)>k:
                    freq[nums[left]]-=1
                    if freq[nums[left]]==0:
                        del freq[nums[left]]
                    left=left+1
                cnt=cnt +(right-left+1)
            return cnt
        return atmost(k)- atmost(k-1)


