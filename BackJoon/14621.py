import sys

N, M = map(int, sys.stdin.readline().split(" "))

# 서로조 집합 자료구조 연산
parent = [0 for _ in range(N+1)]
for i in range(0, N+1):
    parent[i] = i
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, A, B):
    A = find(parent, A)
    B = find(parent, B)
    if A < B:
        parent[B] = A
    else:
        parent[B] = A


gender = [0 for _ in range(N+1)]
temp = list(sys.stdin.readline().rstrip().split(" "))
for a in range(N):
    gender[a+1] = temp[a]


relation = []
for b in range(M):
    u, v, d = map(int, sys.stdin.readline().split(" "))
    relation.append([d,u,v])

relation.sort()

path_sum = 0
path_num = 0
for dist, a, b in relation:
    if find(parent, a) != find(parent, b) and gender[a] != gender[b]:
        union(parent, a, b)
        path_sum += dist
        path_num += 1
