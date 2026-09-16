class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        if len(s) == 1: return 1

        sub_set = set()
        long_s = 1
        count = 1

        l, r = 0, 1
        sub_set.add(s[l])
        print(sub_set)

        while l < len(s) and r < len(s):

            
            if s[r] in sub_set:
                sub_set.remove(s[l])
                count -= 1
                l += 1
            else:
                sub_set.add(s[r])
                count += 1
                r += 1
            # print(sub_set)

            long_s = max(count, long_s)

        return long_s