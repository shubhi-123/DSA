class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum>num*9:
            return ""
        k=sum//9
        rem=sum%9
        ans="9"*k
        if rem>0:
            ans=ans+str(rem)
        ans=ans+"0"*(num-len(ans))
        return ans