class Solution:
    def countAndSay(self, n: int) -> str:
        def f(s):
            l=[]
            i=0
            cnt=1
            while i<len(s)-1:
                if s[i]==s[i+1]:
                    cnt=cnt+1
                else:
                    l.append([cnt, s[i]])
                    cnt=1
                i=i+1
            l.append([cnt, s[i]])
            res=""
            for i,j in l:
                res=res+str(i)+j
            return res
        
        if n==1:
            return "1"
        s="1"
        for _ in range(n-1):
            s=f(s)
        return s

        


