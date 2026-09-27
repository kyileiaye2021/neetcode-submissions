class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # cycle detection
        # undirected edges
        # {1:3}
        # {3:1}

        # count 
        # dfs(n, map, visited)
        #   if n is visited:
        #       return False
        #   visited.add(n)
        #   for nei in map[n]:
        #       res = dfs(nei, map, visited)
        #       if not res
        #           return false
        #   return true

        # iterate thru edges
        #   map[x].append(y)
        #   map[y].append(x)

        # return dfs(0, map, visited)
        def dfs(i, parent, map, visited):

            if i in visited:
                return False

            visited.add(i)

            for nei in map[i]:
                if nei != parent:
                    res = dfs(nei, i, map, visited)
                    if not res:
                        return False

            return True

        map = defaultdict(list)

        for x, y in edges:
            map[x].append(y)
            map[y].append(x)

        visited = set()
        res = dfs(0, None, map, visited)
        return res if len(visited) == n else False

        