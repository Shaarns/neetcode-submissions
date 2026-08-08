class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_count = 0
        l, r = 0, 0
        window = set()

        while r < len(s):
            while s[r] in window:
                window.remove(s[l])
                l += 1
            
            window.add(s[r])
            max_count = max(r-l + 1, max_count)
            r += 1
                
        
        return max_count
    