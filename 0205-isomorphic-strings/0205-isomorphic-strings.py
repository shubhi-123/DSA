class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        stot={}
        ttos={}
        for i in range(len(s)):
            if s[i] in stot:
                if stot[s[i]]!=t[i]:
                    return False
            else:
                stot[s[i]]=t[i]
            if t[i] in ttos:
                if ttos[t[i]]!=s[i]:
                    return False
            else:
                ttos[t[i]]=s[i]
        return True

    