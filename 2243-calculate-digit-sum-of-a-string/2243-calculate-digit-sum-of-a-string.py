class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s)>k:
            res=""
            for i in range(0,len(s),k):
                group=s[i:i+k]
                res+=str(sum(int(d) for d in group))
            s=res
        return s