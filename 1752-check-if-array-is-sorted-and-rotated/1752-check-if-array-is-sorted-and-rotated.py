class Solution:
    def check(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            new=[]
            for idx in range(i,len(nums)):
                new.append(nums[idx])
            for idx in range(i):
                new.append(nums[idx])
            is_sorted=True
            for idx in range(len(nums)-1):
                if new[idx]>new[idx+1]:
                    is_sorted= False
                    break
            if is_sorted:
                return True
        return False

