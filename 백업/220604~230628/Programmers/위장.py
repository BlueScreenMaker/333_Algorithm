from functools import reduce

def multiply(arr):
    return reduce(lambda x, y: x * y, arr)
# 만약 모자가 2개이고 신발이 1개이면 → 2*1 해줌

def solution(clothes):
    answer=0

    kind=[]
    for v in range(0,len(clothes)):
        if not clothes[v][1] in kind:
            kind.append(clothes[v][1])
    # 옷 종류 넣기

    clothes_list=[[] for b in range(0,len(kind))]
    for z in range(0,len(clothes)):
        if clothes[z][1] in kind:
            a=kind.index(clothes[z][1])
            clothes_list[a].append(clothes[z][0])
    # 종류 별로 옷을 분류함

    if len(clothes_list)>1:
        size_list=[]
        for h in range(0,len(clothes_list)):
            size_list.append(len(clothes_list[h])+1)
        answer+=multiply(size_list)
        answer-=1
    # 종류가 1개 이상인 경우, 
    # 각 종류별로 벗을 수 있는 경우의 수를 추가(+1)
    # 각 종류별로 벗을 수 있는 경우가 생겼으므로 모든 종류의 옷을 입지 않는 경우가 생김 → -1로 해당 경우의 수를 뺌

    
    else:
        answer+=len(clothes)
    # 종류가 1개이면 주어진 옷만 입고 벗으면 되므로 이 경우에는 그냥 옷 수만큼의 경우의 수가 생김

    return answer

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))