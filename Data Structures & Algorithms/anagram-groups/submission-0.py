class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_map = {}

        for s in strs:
            sorteds = "".join(sorted(s))
            print(sorteds)
            if sorteds in sorted_map:
                sorted_map[sorteds].append(s)
            else:
                sorted_map[sorteds] = [s]

        return [_ for _ in sorted_map.values()]