class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return False

        adj = {i:[] for i in range(n)}

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        #{0: [1, 2, 3], 1: [0, 4], 2: [0], 3: [0], 4: [1]}
        visited = set()
        def dfs(curr_n, prev_n):
            if curr_n in visited:
                return False

            visited.add(curr_n)

            for nei in adj[curr_n]:
                if nei == prev_n:
                    continue
                if not dfs(nei, curr_n):
                    return False
            return True

        return dfs(0, -1) and n == len(visited)

        

