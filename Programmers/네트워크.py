from collections import deque

def bfs(n,computers,com,visited):
    que=deque()
    que.append(com)
    while que:
        check=que.pop()
        visited[check]=True
        for a in range(n):
            if a!=check and computers[check][a]==1:
                if(visited[a]==False):
                    que.append(a)

def solution(n, computers):
    answer = 0
    visited=[False for _ in range(n)]
    for i in range(n):
        if visited[i]==False:
            visited[i]=True
            bfs(n,computers,i,visited)
            answer+=1
    return answer

print(solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))