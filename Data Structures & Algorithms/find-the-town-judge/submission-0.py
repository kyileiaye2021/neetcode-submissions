class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # happy cases

        # edge cases
        # input: n = 1, trust = [[1,1]]
        # output: -1

        # input: n = 3, trust = [[1,3], [2,3], [3,1], [3,2]]

        # hashmap {a: b}
        # iterate thru the trust
        #   add the first value as key and second as value

        # iterate until n
        #   check if which num is doesn't appear

        # iterate the hashmap 
        #   check if the values are the same as the num that doesn't appear

        judge = 0
        map = {}
        for a, b in trust:
            map[a] = b

        for i in range(1, n+1):
            if i not in map:
                if judge != 0:
                    return -1
                else:
                    judge = i

        for b in map.values():
            if b != judge:
                return -1
        return judge
                 
