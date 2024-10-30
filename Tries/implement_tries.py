class Node:
    def __init__(self, letter):
        self.letter = letter
        self.neighbors = {}

    def insert_neighbor(self, node):
        self.neighbors[node.letter] = node

    def __str__(self):
        return f"Node({self.letter}, children={str(self.neighbors)})"
    
    def get_neighbor(self, l):
        if l in self.neighbors:
            return self.neighbors[l]
        else:
            return None
        

class Trie:

    def __init__(self):
        self.trees = {}

    def insert(self, word: str) -> None:
        if word[0] not in self.trees:
            self.trees[word[0]] = Node(word[0])
        cur = self.trees[word[0]]

        word += "0"

        for i in range(1, len(word)):
            next_n = cur.get_neighbor(word[i])
            if next_n is None:
                next_n = Node(word[i])
                cur.insert_neighbor(next_n)
            cur = next_n

    def traverse(self, word, full=False):
        if word[0] not in self.trees:
            return False
        else:
            cur = self.trees[word[0]]

            for i in range(1, len(word)):
                cur = cur.get_neighbor(word[i])

                if not cur:
                    return False
            
            return cur.get_neighbor("0") is not None if full else True

    def search(self, word: str) -> bool:
        return self.traverse(word, True)

    def startsWith(self, prefix: str) -> bool:
        return self.traverse(prefix)
