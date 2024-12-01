import sys

class Node(object):
    def __init__(self, key):
        self.key = key
        self.children = {}
        self.is_end = False

class Trie(object):
    def __init__(self):
        self.root = Node(None)

    def insert(self, number):
        current_node = self.root

        for num in number:
            if num not in current_node.children:
                current_node.children[num] = Node(num)
            current_node = current_node.children[num]
            if current_node.is_end:
                return False
        current_node.is_end = True

        if current_node.children:
            return False
        else:
            return True

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    logic = Trie()
    result = True
    for _ in range(N):
        temp = sys.stdin.readline().rstrip()
        check = logic.insert(temp)
        if not check:
            result = False
    if result:
        print("YES")
    else:
        print("NO")

