def solution(s):
    answer = 0
    for i in range(len(s)):
        words=s[i:]+s[:i]
        open=['(','[','{']
        close=[')',']','}']
        stack=[]
        flag=False # }}} 같이 닫힌 애들만 나오면 리스트는 비어있지만, 짝이 맞는건 아니니까 거르기 위해 사용
        for j in words:
            if j in open:
                stack.append(j)
            else:
                if stack:
                    if stack[-1]==open[close.index(j)]:
                        flag=True
                        stack.pop()
                    else:
                        flag=False
                else:
                    flag=False
        if len(stack)==0 and flag:
            answer+=1


    return answer

print(solution("[](){}"))