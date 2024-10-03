import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)
nodes= []

while True:
    try:
        nodes.append(int(input()))
    except:
        break

def check(start, end):
    if start > end:
        return
    mid = end + 1
    # 루트 노드보다 작은 노드밖에 없다면,
    # 위의 if 조건에 따라 빠져나올 수 있도록 설정
    for i in range(start+1, end):
        if nodes[i] > nodes[start]:
            mid = i
            break
    check(start, mid-1)
    check(mid, end)
    print(nodes[start])

check(0, len(nodes))