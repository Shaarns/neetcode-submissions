class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digit_to_letter = {
            "2": 'abc',#0 - a, b, ""
            "3": 'def',#1 - ad, ae, af, bd, be, bf ...
            "4": 'ghi',
            "5": 'jkl',
            "6": 'mno',
            "7": 'pqrs',
            "8": 'tuv',
            "9": 'wxyz',
        }

        def backtrack(i, curr_char):
            if len(curr_char) == len(digits):
                res.append(curr_char)
                return


            for c in digit_to_letter[digits[i]]:
                backtrack(i+1, curr_char + c)

        if digits:
            backtrack(0, "")

        return res

            
