class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        # create a graph for the words
        adj_graph = {c: set() for w in words for c in w}
        
        for i in range(len(words) - 1):
            # compare 2 adj words
            word1 = words[i]
            word2 = words[i + 1]

            # check invalid cases
            # prefix of word1 len must be less than that of word2 len
            min_len = min(len(word1), len(word2))

            if word1[:min_len] == word2[:min_len] and len(word1) > len(word2):
                return ""

            for c in range(min_len):
            # else we have to connect the characters
                if word1[c] != word2[c]:
                    adj_graph[word1[c]].add(word2[c]) # need to look at only first different character
                    break

        print(adj_graph)
        visited = {} # to keep track of the loop in the graph
        res = []

        def dfs(c):

            if c in visited:
                return visited[c]

            visited[c] = True # visited the node in curr path

            for nei in adj_graph[c]:
                if dfs(nei):
                    return True
            visited[c] = False # remove the node from the curr path before returning (backtrack)

            print(f'{c} is appended')
            res.append(c)


        # iterating thru every single char in the graph and call dfs on it
        for c in adj_graph:

            # invalid if there are loops in the graph
            if dfs(c):
                return ""

        res.reverse() # we have to reverse as we did post order traversing
        return ''.join(res) # need to return str


