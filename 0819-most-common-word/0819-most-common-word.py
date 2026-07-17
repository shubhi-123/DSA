class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        #LEARN HOW TO COUNT USING HASHMAP IN PYTHON (Using counter)

        paragraph=paragraph.lower()
        for ch in "!?',;.":
            paragraph=paragraph.replace(ch, " ")
        words=paragraph.split()
        banned=set(banned)
        count=Counter()
        for word in words:
            if word not in banned:
                count[word]=count[word]+1
        return count.most_common(1)[0][0]

        #LEARN HOW TO COUNT USING HASHMAP IN PYTHON (Without using counter)

        # freq = {}
        # for word in words:
        #     if word not in banned:
        #         freq[word] = freq.get(word, 0) + 1
        # ans = ""
        # maxi = 0
        # for word in freq:
        #     if freq[word] > maxi:
        #         maxi = freq[word]
        #         ans = word
        # return ans