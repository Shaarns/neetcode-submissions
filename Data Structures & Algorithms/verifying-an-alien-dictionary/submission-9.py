class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        rank = {}
        for i, c in enumerate(order):
            rank[c] = i

        def compare(word1, word2):
            i = 0
            while i < len(word1) and i < len(word2) and word1[i] == word2[i]:
                i += 1

            print(i)
            if i == len(word1):
                return True
            
            if i == len(word2):
                return False

            if rank[word1[i]] > rank[word2[i]]:
                return False

            return True
    
        
        for i in range(len(words) - 1):
            if not compare(words[i], words[i+1]):
                return False

        return True
