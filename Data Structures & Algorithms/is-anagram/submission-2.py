class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        ch_count = {}
        for ch in s:
            if ch in ch_count:
                ch_count[ch] += 1
            else:
                ch_count[ch] = 1

        for ch in t:
            if ch not in ch_count:
                return False
                
            ch_count[ch] -= 1
            if ch_count[ch] < 0:
                return False
        return True