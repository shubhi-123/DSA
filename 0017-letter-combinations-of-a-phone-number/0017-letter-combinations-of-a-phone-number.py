class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic={"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6":"mno", "7":"pqrs", "8": "tuv", "9":"wxyz"}
        result=[]
        def backtrack(index, current):
            if len(digits)==index:
                result.append(current)
                return
            letters=dic[digits[index]]
            for letter in letters:
                backtrack(index+1, current+letter)
        backtrack(0, "")
        return result