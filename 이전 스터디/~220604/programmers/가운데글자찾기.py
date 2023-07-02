def solution(s):
    string = list(s)
    point=int(len(string)/2)
    if (len(string)%2==0):
        answer=string[point-1]+string[point]
    else:
        answer=string[int(point)]

    return answer

print(solution("qwer"))