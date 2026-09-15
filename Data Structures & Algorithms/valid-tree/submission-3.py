class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        ed_map = {i: [] for i in range(n)}

        for n1, n2 in edges:
            ed_map[n1].append(n2)
            ed_map[n2].append(n1)

        visited = set()
        #{0: [1, 2, 3], 1: [0, 4], 2: [0], 3: [0], 4: [1]}

        def dfs(curr_n, prev_n):
            if curr_n in visited:
                return False

            visited.add(curr_n)
            for n in ed_map[curr_n]:
                if n == prev_n:
                    continue
                if not dfs(n, curr_n):
                    return False
            return True

        return dfs(0, -1) and n == len(visited)