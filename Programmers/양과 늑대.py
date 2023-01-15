import sys
sys.setrecursionlimit(10**6)

answer = []

def dfs(edge, visited, info, sheep_count, wolf_count):
    if sheep_count <= wolf_count:
        return
    else:
        answer.append(sheep_count)

    for parent, child in edge:
        if visited[parent] and not visited[child]:
            visited[child] = 1
            if info[child]:
                dfs(edge, visited, info, sheep_count, wolf_count+1)
            else:
                dfs(edge, visited, info, sheep_count+1, wolf_count)
            visited[child] = 0

def solution(info, edges):
    visited = [0 for _ in range(len(info))]
    visited[0] = 1
    dfs(edges, visited, info, 1, 0)
    return max(answer)

print(solution([0,0,1,1,1,0,1,0,1,0,1,1],[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))
print(solution([0,1,0,1,1,0,1,0,0,1,0], [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]))