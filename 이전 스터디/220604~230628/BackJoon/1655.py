import sys
import heapq

N=int(sys.stdin.readline())

leftHeap=[]
rightHeap=[]
answer=[]
for i in range(N):
    inputNum=int(sys.stdin.readline())

    if len(leftHeap)==len(rightHeap):
        heapq.heappush(leftHeap, (-inputNum, inputNum))
    else:
        heapq.heappush(rightHeap, (inputNum, inputNum))

    # left 힙은 중간값보다 작은 값이 들어가고
    # right 힙은 중간값보다 큰 값이 들어가야함
    # 그렇기 때문에 바꾸는게 필요하다~
    if rightHeap and leftHeap[0][1] > rightHeap[0][0]:
        min=heapq.heappop(rightHeap)[0]
        max=heapq.heappop(leftHeap)[1]
        heapq.heappush(leftHeap, (-min, min))
        heapq.heappush(rightHeap, (max, max))

    answer.append(leftHeap[0][1])

for j in answer:
    print(j)


# 파이썬의 heapq 에서는 최소힙은 제공하지만 최대힙은 제공하지않아서 음수로 치환하는 것,
# min힙 같은 경우 - 붙일 필요는 없음!!