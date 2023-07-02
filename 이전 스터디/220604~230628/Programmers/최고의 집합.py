def solution(n, s):
    answer = []

    if n>s:
        return [-1]

    element=s//n
    for i in range(n):
        answer.append(element)

    redundancy=s%n
    index=len(answer)-1
    while redundancy>0:
        answer[index]+=1
        redundancy-=1
        index-=1

    return answer

print(solution(2,9))