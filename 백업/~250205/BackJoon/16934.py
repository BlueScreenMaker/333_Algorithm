import sys
from collections import defaultdict

N = int(sys.stdin.readline())
name = []
for _ in range(N):
    name.append(sys.stdin.readline().rstrip())

# key = 상위 알파벳
# data = 최종 완성된 문자열
# children = 자식 노드 집합
class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.date = data
        self.children = {}

class Trie(object):
    # 루트 설정
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        now = self.head
        for char in string:
            if char not in now.children:
                now.children[char] = Node(char)
            now = now.children[char]
        now.date = string
        # 중복 닉네임 뒤에 번호 붙여야하니 번호 지정
        same_nick[string] += 1

    def search(self, string):
        now = self.head
        result = ''
        for char in string:
            result += char
            print(f"char {char} {now.children}")
            if char in now.children:
                now = now.children[char]
            else:
                return result
        if now.date != None:
            # dict의 초기값이 0부터 시작해서 1 더해줌
            result += str(same_nick[string] + 1)
        return result

check = Trie()
same_nick = defaultdict(int)
for i in range(N):
    print(check.search(name[i]))
    check.insert(name[i])