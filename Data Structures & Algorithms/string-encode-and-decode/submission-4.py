class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStr = ''

        for st in strs:
            charSize = len(st)
            encodedStr += (str(charSize) + '#' + st)

        print(encodedStr)
        return encodedStr

        # '5#Hello5#World'

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0;

        while i < len(s):

            j = i
            while s[j] != '#':
                j += 1
            charLen = int(s[i:j])
            res.append(s[j+1: j+ charLen + 1])
            i = charLen + j + 1 #0+4+1+1=6, 6+7+1+
        print(res)
        return res

        
