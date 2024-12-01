from collections import deque

def bfs(check, target, words, visited):
    que = deque()
    que.append([check, 0])

    while que:
        next, c_count = que.popleft()
        if next == target:
            return c_count
        for i in range(len(words)):
            diff_count = 0
            for c, n in zip(next, words[i]):
                if c!=n:
                    diff_count+=1
            if diff_count == 1:
                visited[i] = True
                que.append([words[i], c_count+1])

def solution(begin, target, words):
    if target not in words:
        return 0
    visited = [False for _ in range(len(words))]
    answer = bfs(begin, target, words, visited)
    return answer

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))