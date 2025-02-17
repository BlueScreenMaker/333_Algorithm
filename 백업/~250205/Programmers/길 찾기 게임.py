import sys
sys.setrecursionlimit(10**6)
# 전위 순회
def pre_order(Y_sort, X_sort, per_answer):
    root = Y_sort[0]
    standard = X_sort.index(root)
    temp1 = []
    temp2 = []

    for i in range(1, len(Y_sort)):
        # 왼쪽
        if root[0] > Y_sort[i][0]:
            temp1.append(Y_sort[i])
        # 오른쪽
        else:
            temp2.append(Y_sort[i])
    # 중심 노드 번호 넣어주고
    per_answer.append(root[2])
    if len(temp1) > 0:
        pre_order(temp1, X_sort[:standard], per_answer)
    if len(temp2) > 0:
        pre_order(temp2, X_sort[standard+1:], per_answer)
    return

# 후위 순회
def post_order(Y_sort, X_sort, post_answer):
    root = Y_sort[0]
    standard = X_sort.index(root)
    temp1 = []
    temp2 = []

    for i in range(1, len(Y_sort)):
        if root[0] > Y_sort[i][0]:
            temp1.append(Y_sort[i])
        else:
            temp2.append(Y_sort[i])

    if len(temp1) > 0:
        post_order(temp1, X_sort[:standard], post_answer)
    if len(temp2) > 0:
        post_order(temp2, X_sort[standard+1:], post_answer)

    post_answer.append(root[2])
    return

def solution(nodeinfo):
    #node 값 넣어주기
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i+1)

    # Y값은 내림 차순으로 정렬 (제일 꼭대기에 있는 노드부터 하나씩 봄)
    Y_sort = sorted(nodeinfo, key=lambda x:(-x[1], x[0]))
    # X값은 오름 차순으로 정렬 (제일 왼쪽에 있는 노드부터 봄)
    X_sort = sorted(nodeinfo)

    pre_answer = []
    post_answer = []

    pre_order(Y_sort, X_sort, pre_answer)
    post_order(Y_sort, X_sort, post_answer)

    return [pre_answer, post_answer]

print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))