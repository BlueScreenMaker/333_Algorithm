import heapq
def solution(scoville, K):
    sort_sco=sorted(scoville)
    heap=[]
    for i in sort_sco:
        heapq.heappush(heap,i)
    answer = 0
    global flag
    flag=False
    while True:
        if len(heap)>0:
            check = heapq.heappop(heap)
            if(check>=K):
                flag=True
                break
            else:
                if(len(heap)>=1):
                    add=heapq.heappop(heap)
                    new=check+(add*2)
                    heapq.heappush(heap,new)
                    answer+=1
                else:
                    break
        else:
            break
    if not flag:
        return -1
    else:
        return answer

print(solution([1,2,3],11))