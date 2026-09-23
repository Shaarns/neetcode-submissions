class Solution:
    def countSubstrings(self, s: str) -> int:
        len_ = len(s)
        num_of_palin = 0

        for i in range(len_):
            l, r = i, i
            while l >= 0 and r < len_ and s[l] == s[r]:
                num_of_palin += 1
                l -= 1
                r += 1

            l, r = i, i+1
            while l >= 0 and r < len_ and s[l] == s[r]:
                num_of_palin += 1
                l -= 1
                r += 1

        return num_of_palin