def solution(gems):
    answer=[]

    start=0
    end=0

    kind=len(set(gems))
    max=len(gems)+1

    current_gem={}

    while end<len(gems):
        if gems[end] not in current_gem:
            current_gem[gems[end]]=1
        else:
            current_gem[gems[end]]+=1

        end+=1

        if len(current_gem)==kind:
            while start<end:
                if current_gem[gems[start]]>1:
                    current_gem[gems[start]]-=1
                    start+=1
                elif max>end-start:
                    max=end-start
                    answer=[start+1,end]
                    break
                else:
                    break

    return answer

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))

'''
# 시간 초과 풀이
def solution(gems):
    result = []

    kind=set(gems)

    for i in range(len(gems)):
        type=[]
        for j in range(i,len(gems)):
            if not gems[j] in type:
                type.append(gems[j])
                if len(type)==len(kind):
                    result.append([abs(i-j),i+1,j+1])
                    break

    result.sort(key=lambda x:x[0])
    answer=[result[0][1],result[0][2]]
    return answer
'''