import sys
from collections import defaultdict


class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}

class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        current_node = self.head

        for char in string:
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]
        current_node.data = string
        same_nick[string] += 1

    def search(self, string):
        current_node = self.head
        result = ""
        for char in string:
            result += char
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return result
        if current_node.data != None:
            result += str(same_nick[string] + 1)
        return result

N = int(sys.stdin.readline())
same_nick = defaultdict(int)
check = Trie()
for i in range(N):
    name = sys.stdin.readline().rstrip()
    print(check.search(name))
    check.insert(name)
