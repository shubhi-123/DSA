class Solution:
    def numDecodings(self, s: str) -> int:
        n=len(s)
        dp=[-1]*n
        def solve(i):
            if i==n:
                return 1
            if s[i]=="0":
                return 0
            if dp[i]!=-1:
                return dp[i]
            ans=solve(i+1)
            if i+1<n and 10<=(int(s[i:i+2]))<=26:
                ans=ans+solve(i+2)
                dp[i]=ans
            return ans
        return solve(0)