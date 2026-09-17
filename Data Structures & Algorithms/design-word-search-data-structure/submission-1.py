class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()

            curr = curr.children[c]
        curr.endofWord = True

    def helper(self, word, j, root):
        
        curr = root

        for i in range(j, len(word)):

            # if char == '.' --> try every node in curr
            if word[i] == '.':
                for child in curr.children.values():
                    if self.helper(word, i + 1, child):
                        return True
                return False

            else:
                if word[i] not in curr.children:
                    return False
                curr = curr.children[word[i]]

        return curr.endofWord

    def search(self, word: str) -> bool:
        return self.helper(word, 0, self.root)

        
