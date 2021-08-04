def solution(tickets):
    tickets=sorted(tickets, key=lambda x:x[1], reverse=True)
    router=dict()
    for start,end in tickets:
        if start in router:
            router[start].append(end)
        else:
            router[start]=[end]

    answer = []
    temp=["ICN"]
    while temp:
        check=temp[-1]
        if check not in router or len(router[check])==0:
            answer.append(temp.pop())
        else:
            temp.append(router[check].pop())
    return answer[::-1]


print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
# print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
# print(solution([["ICN", "BBB"],["ICN", "CCC"],["BBB", "CCC"],["CCC", "BBB"],["CCC", "ICN"]]))

'''
def set_arrvie(tickets,visited,check,index,N):
    que=deque()
    visited[index][0]=True
    visited[index][1]=True
    que.append(check)

    while que:
        point=que.popleft()
        answer.append(point)
        for i in range(0,N):
            if point in tickets[i][0]:
                if not visited[i][0] and not visited[i][1]:
                    que.append(tickets[i][1])
                    visited[i][0]=True
                    visited[i][1]=True
                    break


def solution(tickets):
    N=len(tickets)

    visited=[[False,False] for _ in range (N)]

    tickets=sorted(tickets, key=lambda x:x[1])

    answer.append("ICN")
    position=0

    for i in range(0,N):
        if tickets[i][0]=="ICN":
            position=i
            break

    set_arrvie(tickets,visited,tickets[position][1],position,N)

    return answer
'''
