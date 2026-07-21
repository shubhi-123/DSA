class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        arr=[]
        n=len(nums)
        nums.sort()
        j=0
        k=-1
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=n-1
            while j<k:
                total=nums[i] + nums[j] + nums[k]
                if total>0:
                    k=k-1
                elif total<0:
                    j=j+1
                else:
                    arr.append([nums[i], nums[j], nums[k]])
                    j=j+1
                    while nums[j]==nums[j-1] and j<k:
                        j=j+1
        return arr






        