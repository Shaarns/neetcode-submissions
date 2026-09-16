class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_s = set()
        l = 0
        long_s = 0

        for r in range(len(s)):
            
            while s[r] in sub_s:
                sub_s.remove(s[l])
                l += 1

            sub_s.add(s[r])
            long_s = max(long_s, r - l + 1)

        return long_s

