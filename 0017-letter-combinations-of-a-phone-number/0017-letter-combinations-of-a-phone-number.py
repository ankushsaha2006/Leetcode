class Solution(object):
    def letterCombinations(self, digits):
        
        char = {"2":"abc",
                "3":"def",
                "4":"ghi",
                "5":"jkl",
                "6":"mno",
                "7":"pqrs",
                "8":"tuv",
                "9":"wxyz"}
        if not digits:
            return []

        result = []
        def backcheck(index,current):
            if index==len(digits):
                result.append(current)
                return
            letter = char[digits[index]]
            for ch in letter :
                backcheck(index+1,current+ch)
        backcheck(0,"")
        return result