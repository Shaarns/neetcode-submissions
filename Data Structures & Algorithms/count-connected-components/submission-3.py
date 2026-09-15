class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ed_map = {i: [] for i in range(n)}

        for n1, n2 in edges:
            ed_map[n1].append(n2)
            ed_map[n2].append(n1)

        print(ed_map)
        visited = set()
        #{0: [1, 2], 1: [0, 2], 2: [1, 0], 3: [4], 4: [3]}

        def dfs(curr_n):
            if curr_n in visited:
                return

            visited.add(curr_n)
            for n in ed_map[curr_n]:
                dfs(n)

        count = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1

        return count
