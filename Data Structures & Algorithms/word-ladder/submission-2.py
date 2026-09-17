class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # create patterns for each word

        if endWord not in wordList:
            return 0

        wordList.append(beginWord)
        pattern_map = defaultdict(list)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + '*' + word[j + 1:] 
                pattern_map[pattern].append(word)

        # BFS
        visit = set()
        queue = deque()
        queue.append((beginWord, 1))

        while queue:
            word, length = queue.popleft()

            if word == endWord:
                return length

            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]

                for nei in pattern_map[pattern]:
                    if nei not in visit:
                        visit.add(nei)
                        queue.append((nei, length + 1))

        return 0



