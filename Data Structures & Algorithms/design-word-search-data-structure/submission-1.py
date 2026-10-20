class TrieNode:
    children: dict[char, TrieNode]
    isWord: bool

    def __init__(self, word: str = ""):
        self.children = {}
        self.isWord = True
        if len(word) == 0:
            return
        
        rest = word[1:]
        node = TrieNode(rest)
        child = word[0]
        self.children[child] = node
        self.isWord = False

class WordDictionary:

    root: TrieNode
    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        node: TrieNode = self.root
        while len(word) > 0 and word[0] in node.children.keys():
            node = node.children[word[0]]
            word = word[1:]
        
        if len(word) == 0:
            node.isWord = True
        else:
            node.children[word[0]] = TrieNode(word[1:])
        

    def search(self, word: str) -> bool:

        nodes: List[TrieNode] = [self.root]
        nextNodes = []

        #print(f"Searching for: {word}")
        while len(word) > 0 and len(nodes) > 0:
            letter = word[0]

            #print(f"Searching : {letter}, nodes: {len(nodes)}")
            word = word[1:]
            for node in nodes:
                if letter == ".":
                    nextNodes.extend(node.children.values())
                elif letter in node.children.keys():
                    nextNodes.append(node.children[letter])
            
            nodes = nextNodes
            nextNodes = []

        #print(f"done searching: word: {word}, nodes: {len(nodes)}")
        
        if len(word) > 0:
            return False
        
        found: bool = False
        for node in nodes:
            if node.isWord:
                return True

        #print(f"search {word}, found: {found}")
        return False
        
        


