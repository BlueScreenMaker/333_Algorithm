import sys
sys.setrecursionlimit(10**9)

N, S, D = map(int, sys.stdin.readline().split(" "))

relation=[[] for _ in range(N + 1)]

for i in range(N-1):
    a,b=map(int,sys.stdin.readline().split())
    relation[a].append(b)
    relation[b].append(a)

visited = [False for _ in range(N+1)]
depth = [0 for _ in range(N+1)]

def dfs(node):
    count = 0
    for next in relation[node]:
        if not visited[next]:
            visited[next] = True
            count = max(count, dfs(next))
    depth[node] = count
    return depth[node] + 1

visited[S] = True
dfs(S)
answer = 0
print(depth)
for i in range(1, N+1):
    if i != S and depth[i] >= D:
        answer += 1

# 왕복이라서
print(answer * 2)