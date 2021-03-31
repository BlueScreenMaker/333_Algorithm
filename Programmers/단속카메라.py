def solution(routes):
    routes=sorted(routes, key=lambda x:x[1])
    point=routes[0][1]
    answer=1
    for i in range(1,len(routes)):
        if point<routes[i][0]:
            point=routes[i][1]
            answer+=1
    return answer

print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]))