import sys
sys.setrecursionlimit(10**6)

def bfs(vistied, relation, node ,dp):
    visited[node] = True
    dp[node][1] = 1
    dp[node][0] = 0
    for child in relation[node]:
        if not visited[chlid]:
            bfs(visited, relation, child)
            dp[node][0] += dp[child][1]
            dp[node][1] += min(dp[child][0], dp[child][1])

def solution(n, lighthouse):
    answer = 0

    vistied = [False for _ in range(n+1)]

    relation = [[] for _ in range(n+1)]
    for i in range(len(lighthouse)):
        a, b = lighthouse[i]
        relation[a].append(b)
        relation[b].append(a)
    
    dp = [[0,0] for _ in range(n+1)]

    dfs(visited, relation, 1, dp)
    return min(dp[1])

print(solution(8, [[1, 2], [1, 3], [1, 4], [1, 5], [5, 6], [5, 7], [5, 8]]))