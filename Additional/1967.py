import sys
from collections import deque

N = int(sys.stdin.readline())

graph = [[] for _ in range(N+1)]
for i in range(N-1):
    a, b, c = map(int, sys.stdin.readline().split(" "))
    graph[a].append([b,c])
    graph[b].append([a,c])

def bfs(start):
    visited = [False] * (N+1)
    que = deque()
    que.append([start,0])

    more_far_node = start
    max_dist = 0

    visited[start] = True

    while que:
        c_node, c_dist = que.popleft()
        for next, weight in graph[c_node]:
            if not visited[next]:
                visited[next] = True
                next_dist = c_dist + weight
                que.append([next, next_dist])
                if next_dist > max_dist:
                    max_dist = next_dist
                    more_far_node = next

    return max_dist, more_far_node

# 첫번째 노드에서 가장 먼 노드 찾기 == 끝점
_, next_node = bfs(1)

# 끝점에서 가장 먼 노드 찾기
tree_dist, _ = bfs(next_node)
print(tree_dist)