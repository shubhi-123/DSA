class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums)%k!=0:
            return False
        nums.sort()
        freq={}
        for num in nums:
            freq[num]=freq.get(num, 0)+1
        for num in nums:
            if freq[num]==0:
                continue
            for i in range(num, num+k):
                if freq.get(i,0)==0:
                    return False
                freq[i]=freq[i]-1
        return True