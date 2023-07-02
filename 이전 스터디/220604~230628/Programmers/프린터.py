def solution(priorities, location):
    answer = 0

    while priorities:
        if location==0:
            if priorities[0]<max(priorities):
                priorities.append(priorities.pop(0))
                location=len(priorities)-1
            else:
               return answer+1
        else:
            if priorities[0]<max(priorities):
                priorities.append(priorities.pop(0))
                location-=1
            else:
                priorities.pop(0)
                location-=1
                answer+=1

print(solution([2, 1, 3, 2],2))
print(solution([1, 1, 9, 1, 1, 1],0))