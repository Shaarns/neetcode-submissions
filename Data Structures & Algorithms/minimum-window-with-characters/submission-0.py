class Solution:
    def minWindow(self, s: str, t: str) -> str:
        min_len = float('inf')
        res = []
        count_s = {}
        count_t = {}

        for ch in t:
            count_t[ch] = count_t.get(ch, 0) + 1

        need = len(count_t)
        have = 0
        l = 0

        for r in range(len(s)):
            if s[r] in count_t:
                count_s[s[r]] = count_s.get(s[r], 0) + 1

                if count_s[s[r]] == count_t[s[r]]:
                    have += 1

                while need == have:
                    if min_len > r - l + 1:
                        min_len = r - l + 1
                        res = [l, r]

                    if s[l] in count_s:

                        if count_s[s[l]] == count_t[s[l]]:
                            have -= 1

                        count_s[s[l]] -= 1
                    l += 1
        if not res:
            return ""

        return s[res[0]: res[1] + 1]



