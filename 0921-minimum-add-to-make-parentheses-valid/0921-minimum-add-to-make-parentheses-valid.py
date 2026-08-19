class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        res=0
        cnt=0
        for ch in s:
            if ch=="(":
                cnt=cnt+1
            else:
                if cnt>0:
                    cnt=cnt-1
                else:
                    res=res+1
        return res+cnt

