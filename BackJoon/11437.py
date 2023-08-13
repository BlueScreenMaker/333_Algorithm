import sys
sys.setrecursionlimit(100000)

N = int(sys.stdin.readline()) # 노드의 수

relationship = [[] for _ in range(N+1)]
for _ in range(N-1): # 간선 정보
    a, b = map(int, sys.stdin.readline().split(" "))
    relationship[a].append(b)
    relationship[b].append(a)

parent = [0 for _ in range(N+1)] # 각 노드의 부모 노드
depth = [0 for _ in range(N+1)] # 루트노드에서 각 노드까지의 깊이
visited = [0 for _ in range(N+1)]

# 루트노드에서 각 노드까지의 깊이 구하기
def find_depth(node, depth_count):
    visited[node] = True
    # 깊이 갱신
    depth[node] = depth_count

    for check in relationship[node]:
        if not visited[check]:
            parent[check] = node
            find_depth(check, depth_count+1)

def LCA(a,b):
    # 두 노드의 깊이 맞추기
    while depth[a] != depth[b]:
        if depth[a] > depth[b]:
            a = parent[a]
        else:
            b = parent[b]

    while a != b:
        a = parent[a]
        b = parent[b]

    return a

find_depth(1,0)
M = int(sys.stdin.readline()) # 공통조상을 알고싶은 쌍의 개수
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split(" "))
    print(LCA(a,b))