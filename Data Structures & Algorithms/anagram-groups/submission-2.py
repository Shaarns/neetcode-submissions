class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}

        for s in strs:
            list_of_alpha = [0] * 26
            for ch in s:
                list_of_alpha[ord(ch) - ord('a')] += 1

            
            ls = tuple(list_of_alpha)
            if ls in group:
                group[ls].append(s)
            else:
                group[ls] = [s]
        return [_ for _ in group.values()]




        