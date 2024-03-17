import heapq
import sys

p,w = map(int,sys.stdin.readline().split(" "))

back_c, cube_c = map(int,sys.stdin.readline().split(" "))

parent = [i for i in range(p)]

graph = []

for i in range(w):
    start, end, width = map(int,sys.stdin.readline().split(" "))
    heapq.heappush(graph, (-width, start, end))

def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

def union_parent(parent, x, y):
    node1 = find_parent(parent, x)
    node2 = find_parent(parent, y)

    if node1 < node2:
        parent[node2] = node1
    else:
        parent[node1] = node2

answer = 0

while graph:
    w, s, e = heapq.heappop(graph)
    w = -w
    union_parent(parent, s, e)

    if find_parent(parent, back_c) == find_parent(parent, cube_c):
        answer = w
        break

print(answer)


