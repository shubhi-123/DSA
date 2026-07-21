class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a=min(nums)
        b=max(nums)
        while a>0 and b>0:
            if a>b:
                a=a%b
            else:
                b=b%a
        if b==0:
            return a
        return b