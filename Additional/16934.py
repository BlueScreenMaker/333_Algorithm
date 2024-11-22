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
            # 새로운 문자가 기존 노드의 자식 노드에 없는 경우에만 새로운 노드를 생성
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
            # 문자열 탐색 중 현재 문자가 이미 트라이(Trie) 구조에 존재하는 경우,
            # 해당 문자에 해당하는 자식 노드로 이동하도록 하는 것
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
