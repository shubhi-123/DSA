class Solution:
    def myPow(self, x: float, n: int) -> float:
        def calc(a,b):
            if b==0:
                return 1.0
            half=calc(a,b//2)
            if b%2==0:
                return half*half
            else:
                return half*half*a
        if n<0:
            x=1/x
            n=-n
        return calc(x,n)