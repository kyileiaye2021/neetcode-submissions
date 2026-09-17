class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # iterate thru the equations
        #   {a: {b: a/b}, b: {a: b/a, c: b/c}, c: {b: c/b}}
        equ_map = defaultdict(dict)
        for i, (var1, var2) in enumerate(equations):
            equ_map[var1][var2] = values[i]
            equ_map[var2][var1] =  (1/values[i])

        # iterating thru the equ map
        #   go to the connected vars and find the ones that are not connected to the 
        for i in equ_map:
            equ_map[i][i] = 1 

            for j, k in combinations(equ_map[i], 2):
                if j not in equ_map[k]:
                    equ_map[k][j] = equ_map[i][j] / equ_map[i][k]
                    equ_map[j][k] = 1 / equ_map[k][j]

        print(equ_map)
        res = []
        for u, v in queries:
            if v in equ_map[u]:
                res.append(equ_map[u][v])
            else:
                res.append(-1)

        return res
