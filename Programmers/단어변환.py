def solution(begin, target, words):
    answer = 0
    if not target in words:
        return answer
    else:
        visited=[False for _ in range (len(words))]
        for i in range(0,len(words)):
            if not visited[i]:
                count=0
                for j in range(0,len(words[i])):
                    if begin[j]!=words[i][j]:
                        count+=1
                if count<2:
                    begin=words[i]
                    answer+=1
                    visited[i]=True
                if begin==target:
                    return answer-1

print(solution("hit","cog",["hot", "dot", "dog", "lot", "log","cog"]))