class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # dfs 
        map = defaultdict(list)

        for x, y in edges:
            map[x].append(y)
            map[y].append(x)

        def dfs(i, parent, map, visited):
            if i not in visited:
                visited.add(i)

            for nei in map[i]:
                if nei == parent or nei in visited:
                    continue

                dfs(nei, i, map, visited)

        count = 0
        visited = set()
        for i in range(n):
            if i not in visited:
                dfs(i, None, map, visited)
                count += 1

        return count

                