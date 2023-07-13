class Node(object):
    def __init__(self,key,data=None):
        self.key = key
        self.data = data
        self.children = {}

class Trie(object):
    def __init__(self):
        self.head = Node(None)
    def insert(self,string):
        curr_node = self.head
        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
            curr_node = curr_node.children[char]
        curr_node.data = string

    def starts_with(self,prefix):
        curr_node = self.head
        for char in prefix:
            if curr_node.data:
                return True
            else:
                if char in curr_node.children:
                    curr_node = curr_node.children[char]
                else:
                    return False
        return False
            
    
for _ in range(int(input())):
    n = int(input())
    trie = Trie()
    ans = 'YES'
    arr = []
    for i in range(n):
        tem = input()
        arr.append(tem)
    arr.sort(key=lambda x: len(x))
    for tem in arr:
        if trie.starts_with(tem):
            ans = 'NO'
            break
        else:
            trie.insert(tem)
    print(ans)