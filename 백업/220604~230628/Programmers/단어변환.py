from collections import deque

global answer

def bfs(begin, target, words, visited):
    answer=0
    que=deque()
    que.append(begin)
    while que:
        check=que.pop()
        if check==target:
            return answer
        for i in range(len(words)):
            if visited[i]==True:
                continue
            count=0
            for a,b in zip(check,words[i]):
                if a!=b:
                    count+=1
            if count==1:
                visited[i]=True
                que.append(words[i])
        answer+=1

    return answer

def solution(begin, target, words):
    if not target in words:
        return 0

    visited=[False for _ in words]
    answer=bfs(begin,target,words,visited)
    return answer

print(solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"]))