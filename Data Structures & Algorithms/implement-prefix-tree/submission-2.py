class PrefixTree:

    # dog , do
    # {d: [dog, do]
    #  do: [dog, do]
    #  dog: [dog]}

    def __init__(self):
        # set to store the inserted words: dog, do
        # hashmap to store the substr and a list of words
        self.word_set = set()
        self.search_word = defaultdict(list)

    def insert(self, word: str) -> None:
        # insert the word to word_set
        # iterate thru the char in word
        #   get the substr upto curr char and map to the word
        self.word_set.add(word)
        for i in range(len(word)):
            curr_substr = word[:i + 1]
            self.search_word[curr_substr].append(word)

    def search(self, word: str) -> bool:
        # check if the word is in word_set --> return true
        # otherwise return false
        return word in self.word_set

    def startsWith(self, prefix: str) -> bool:
        # check if the prefix is in search map --> return true
        # otherwise return false
        return prefix in self.search_word