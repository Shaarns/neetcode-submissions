class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        arr = [0] * 26
        obj = {}
        for ch1 in s1:
            obj[ch1] = obj.get(ch1, 0) + 1
            arr[ord(ch1) - ord('a')] += 1
        
        char_count_s1 = tuple(arr)
        
        l = 0
        r = 0
        for r in range(len(s2)):
            while l < len(s2) and s2[l] not in obj:
                l += 1

            if r-l+1 == len(s1):
                arr2 = [0] * 26

                for k in range(l, r + 1):
                    arr2[ord(s2[k]) - ord('a')] += 1

                char_count_s2 = tuple(arr2)

                if char_count_s1 == char_count_s2:
                    return True
                else:
                    l += 1
        return False    

                
            