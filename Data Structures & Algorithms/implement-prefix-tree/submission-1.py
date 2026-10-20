class TrieNode:
    children: dict[char, TrieNode]
    isWord: bool

    def __init__(self, word: str = ""):
        self.children = {}
        self.isWord = True
        if len(word) == 0:
            return
        
        rest = word[1:]
        #print(f"inserting node: {word[0]}")
        node = TrieNode(rest)
        child = word[0]
        self.children[child] = node
        self.isWord = False


class PrefixTree:

    root: TrieNode

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:

        node: TrieNode = self.root
        #print(f"insert: {word}")
        while len(word) > 0 and word[0] in node.children.keys():
            node = node.children[word[0]]
            word = word[1:]
        
        if len(word) == 0:
            node.isWord = True
        else:

            #print(f"inserting node: {word[0]}")
            node.children[word[0]] = TrieNode(word[1:])


    def search(self, word: str) -> bool:
        
        node: TrieNode = self.root

        while len(word) > 0 and word[0] in node.children.keys():
            node = node.children[word[0]]
            word = word[1:]
        
        if len(word) > 0:
            return False

        found = node.isWord

        #print(f"search {word}, found: {found}")
        return found
        

    def startsWith(self, prefix: str) -> bool:

        node: TrieNode = self.root

        while len(prefix) > 0 and prefix[0] in node.children.keys():
            node = node.children[prefix[0]]
            prefix = prefix[1:]
        
        found = (len(prefix) == 0)

        #print(f"starts with {prefix}, found: {found}")
        return found
        
        
        