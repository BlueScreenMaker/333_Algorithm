import sys
read=sys.stdin.readline
import heapq

result=[]
for T in range(int(read())):
    visited=[False]*1_000_001
    minH,maxH=[],[]
    for i in range(int(read())):
        s=read().split()
        if s[0]=='I':
            heapq.heappush(minH,(int(s[1]),i))
            heapq.heappush(maxH,(-int(s[1]),i))
            visited[i]=True
        elif s[1]=='1':
            while maxH and not visited[maxH[0][1]]:heapq.heappop(maxH)
            if maxH:
                visited[maxH[0][1]]=False
                heapq.heappop(maxH)
        else:
            while minH and not visited[minH[0][1]]:heapq.heappop(minH)
            if minH:
                visited[minH[0][1]]=False
                heapq.heappop(minH)
    while minH and not visited[minH[0][1]]:heapq.heappop(minH)
    while maxH and not visited[maxH[0][1]]:heapq.heappop(maxH)
    result.append(f'{-maxH[0][0]} {minH[0][0]}'if maxH and minH else'EMPTY')
print('\n'.join(result))

# for i in range(N):
#     maxQ=[]
#     minQ=[]
#     K=int(sys.stdin.readline())
#     visited=[False] * 1000001
#
#     for j in range(K):
#         input_str=sys.stdin.readline()
#         if input_str[0]=='I':
#             num=int(input_str[2:])
#             heapq.heappush(maxQ,(-num,j))
#             heapq.heappush(minQ,(num,j))
#             visited[j]=True
#         elif input_str[0]=='D':
#             if input_str[2:]=='-1':
#                 while minQ and not visited[minQ[0][1]]:
#                     heapq.heappop(minQ)
#                 if minQ:
#                     visited[minQ[0][1]]=False
#                     heapq.heappop(minQ)
#             else:
#             # elif input_str[2:]=='1':
#                 while maxQ and not visited[maxQ[0][1]]:
#                     heapq.heappop(maxQ)
#                 if maxQ:
#                     visited[maxQ[0][1]]=False
#                     heapq.heappop(maxQ)
#
#     while minQ and not visited[minQ[0][1]]:
#         heapq.heappop(minQ)
#     while maxQ and not visited[maxQ[0][1]]:
#         heapq.heappop(maxQ)
#
#     if minQ and maxQ:
#         print(-maxQ[0][0], minQ[0][0])
#     else:
#         print("EMPTY")