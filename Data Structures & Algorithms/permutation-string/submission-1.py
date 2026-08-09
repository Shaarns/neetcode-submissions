class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        char_count_s1 = [0] * 26
        char_count_s2 = [0] * 26
        for ch1 in s1:
            char_count_s1 [ord(ch1) - ord('a')] += 1
        
        l = 0
        for r in range(len(s2)):
            char_count_s2[ord(s2[r]) - ord('a')] += 1
            
            if r-l+1 > len(s1):
                char_count_s2[ord(s2[l]) - ord('a')] -= 1
                l += 1

            if char_count_s1 == char_count_s2:
                return True
                
        return False    

                
            