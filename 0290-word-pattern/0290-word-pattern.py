class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words=s.split()
        if len(pattern)!=len(words):
            return False
        f1={}
        f2={}
        for p, word in zip(pattern, words):
            if p in f1:
                if f1[p]!=word:
                    return False
            else:
                f1[p]=word
            if word in f2:
                if f2[word]!=p:
                    return False
            else:
                f2[word]=p
        return True        