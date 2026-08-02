class Solution:
    def isValid(self, word: str) -> bool:
        word=word.lower()
        vow=False
        conso=False
        if len(word)<3:
            return False
        vowel="aeiou"
        digi="1234567890"
        alpha="abcdefghijklmnopqrstuvwxyz"
        for char in word:
            if (char not in digi and char not in alpha):
                return False
            if char in vowel:
                vow=True
            if (char not in vowel and char not in digi):
                conso=True
        if vow and conso:
            return True
        return False
