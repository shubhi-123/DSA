class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        c = list(s)
        cnt = 0
        prev = 0
        for i in range(len(s)):
            if s[i] == "(":
                cnt= cnt+ 1
            else:
                cnt=cnt-1
            if cnt == 1 and prev == 0:
                c[i] = ""
                prev = 1
            elif cnt == 0 and prev == 1:
                c[i] = ""
                prev = 0
        return "".join(c)