class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = strs[0]

        for s in strs:
            i = 0

            while i < len(s) and i < len(ans) and ans[i] == s[i]:
                i += 1
            
            ans = ans[:i]

        return ans
            
            

            