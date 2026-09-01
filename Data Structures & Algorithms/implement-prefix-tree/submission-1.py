class PrefixTree:

    def __init__(self):
        self.trie = {} # {d: {o: {g: {.}}}}

    def insert(self, word: str) -> None:
        curr = self.trie
        for c in word:
            if c not in curr:
                curr[c] = {}

            curr = curr[c]
        curr["."] = True

    def search(self, word: str) -> bool:
        curr = self.trie

        for c in word:
            if c not in curr:
                return False
            curr = curr[c]

        return "." in curr

    def startsWith(self, prefix: str) -> bool:
        curr = self.trie

        for c in prefix:
            if c not in curr:
                return False
            curr = curr[c]

        return True
        