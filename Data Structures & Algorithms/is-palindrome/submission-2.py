class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ''
        for ch in s:
            if(ch.isalnum() and ch != ' '):
                newStr += ch.lower()
        print(newStr)

        i = 0
        j = len(newStr) - 1
        print(i, j)

        while i < j:
            if(newStr[i] != newStr[j]):
                return False
            i += 1
            j -= 1
        return True
