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