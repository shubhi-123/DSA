class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans=[]
        def generate(s):
            if len(s)==n:
                ans.append(s)
                return
            generate(s+"1")
            if not s or s[-1]!="0":
                generate(s+"0")
        generate("")
        return ans