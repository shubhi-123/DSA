class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def f(g):
            if g<0:
                return 0
            l=0
            summ=0
            cnt=0
            for r in range(len(nums)):
                summ=summ+nums[r]
                while (summ>g):
                    summ=summ-nums[l]
                    l=l+1
                cnt=cnt+(r-l+1)
            return cnt
        return f(goal)- f(goal-1)
