class TreeNode:
    def __init__(self, val, children):
        self.val = val
        self.children = children
        
class Trie:

    def __init__(self):
        self.root = TreeNode("@", [])

    def insert(self, word: str) -> None:
        word += "."
        head = self.root
        
        for c in word:
            # check if letter is in the tree
            found = False
            for child in head.children:
                if child.val == c:
                    found = True
                    head = child
                    break
            if not found:
                head.children.append(TreeNode(c, []))
                head = head.children[-1]            
            

    def search(self, word: str) -> bool:
        return self.startsWith(word + ".")
        

    def startsWith(self, prefix: str) -> bool:
        head = self.root
        
        for c in prefix:
            found = False
            for child in head.children:
                if child.val == c:
                    found = True
                    head = child
                    break
            if not found:
                return False
            
        return True

test = Trie()

test.insert("apple")

print(test.startsWith("app"))