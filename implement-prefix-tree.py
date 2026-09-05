# implement trie (prefix tree)
# https://neetcode.io/problems/implement-prefix-tree/question
# code by aveia@github

class PrefixTree:

    class Node:
        def __init__(self, end):
            self.end = end
            self.nxt = {}

    def __init__(self):
        self.root = PrefixTree.Node(None)

    def insert(self, word: str) -> None:
        cur = self.root
        while word:
            if len(word) == 1:
                if word not in cur.nxt:
                    cur.nxt[word] = PrefixTree.Node(True)
                else:
                    cur.nxt[word].end = True
            elif word[0] not in cur.nxt:
                cur.nxt[word[0]] = PrefixTree.Node(False)
            cur = cur.nxt[word[0]]
            word = word[1:]

    def search(self, word: str) -> bool:
        node = self.root
        while word:
            if word[0] not in node.nxt:
                return False
            node = node.nxt[word[0]]
            word = word[1:]
        return node.end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        while prefix:
            if prefix[0] not in node.nxt:
                return False
            node = node.nxt[prefix[0]]
            prefix = prefix[1:]
        return True
