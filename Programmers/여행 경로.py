from collections import deque

global answer
answer = []

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

# print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))

# print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))

print(solution([["ICN", "BBB"],["ICN", "CCC"],["BBB", "CCC"],["CCC", "BBB"],["CCC", "ICN"]]))

# global answer
# answer = []
#
# flag=True
#
# def set_arrive(start, ticket, N, visited):
#     temp=[]
#     for i in range(0,N):
#         if start in ticket[i][0]:
#             if not visited[i][0] and not visited[i][1]:
#                 temp.append([ticket[i][1],i])
#     if temp:
#         temp=sorted(temp,key=lambda x:x[0])
#         choice, position=temp[0][0],temp[0][1]
#         visited[position][0]=True
#         visited[position][1]=True
#         answer.append(choice)
#         set_arrive(choice,ticket,N,visited)
#     else:
#         return
#
#
# def solution(tickets):
#     N=len(tickets)
#     visited=[[False,False] for _ in range (N)]
#     answer.append("ICN")
#     set_arrive("ICN",tickets,N,visited)
#     return answer



