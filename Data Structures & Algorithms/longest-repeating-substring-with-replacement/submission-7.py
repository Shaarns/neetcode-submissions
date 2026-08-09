class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        window = [0] * 26
        l = 0

        for r in range(len(s)):
            window[ord(s[r]) - 65] = window[ord(s[r]) - 65] +  1

            while ((r - l + 1) - max(window)) > k:
                window[ord(s[l]) - 65] -= 1
                l += 1

            longest = max(longest, r - l + 1)
        print(window)

        return longest