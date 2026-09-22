class Solution:
    def longestPalindrome(self, s: str) -> str:
        # abbafwaoijf
        #ababd
        max_size = 0
        sub_s, sub_e = 0, 0

        for i in range(len(s)):
            l, r = i, i
            #for odd len
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if max_size < (r - l + 1):
                    max_size = r - l
                    sub_s, sub_e = l, r
                l -= 1
                r += 1


            #for even len
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if max_size < (r - l + 1):
                    max_size = r - l
                    sub_s, sub_e = l, r
                l -= 1
                r += 1

            
        return s[sub_s:sub_e+1]



