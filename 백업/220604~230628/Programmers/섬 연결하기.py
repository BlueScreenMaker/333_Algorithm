def solution(n, costs):
    costs=sorted(costs, key=lambda x:x[2])
    link=set([costs[0][0]])
    total=0

    while len(link)!=n:
        for i in costs:
            if i[0] in link and i[1] in link:
                continue
            if i[0] in link or i[1] in link:
                link.update([i[0],i[1]])
                total+=i[2]
                break
    return total

print(solution(4,[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))