class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n=len(items)
        dp=[0]*(budget+1)
        min_price=min(price for factor,price in items)
        for factor,price in items:
            cnt=sum(f%factor==0 for f,p in items)
            for j in range(budget,price-1,-1):
                dp[j]=max(dp[j],dp[j-price]+cnt)
        return max(dp[i]+(budget-i)//min_price for i in range(budget+1))