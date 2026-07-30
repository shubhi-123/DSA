class Solution:
    def minimumPushes(self, word: str) -> int:
        freq={}
        for char in word:
            freq[char]=freq.get(char,0)+1
        arr=sorted(freq.values(), reverse=True)
        ans=0
        for i in range(len(arr)):
            pushes=i//8 +1
            ans=ans+pushes*arr[i]
        return ans