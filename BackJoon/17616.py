import sys
from collections import deque

N,M,X=map(int,sys.stdin.readline().split())

high=[[] for _ in range(N+1)]
low=[[] for _ in range(N+1)]

for i in range(M):
    a,b=map(int,sys.stdin.readline().split())
    low[a].append(b)
    high[b].append(a)

def lower(l):
    visited = [False] * (N + 1)
    que_low=deque()
    que_low.append(l)
    visited[l]=True
    count=0
    while que_low:
        check_low=que_low.popleft()
        for i in low[check_low]:
            if visited[i]==False:
                visited[i]=True
                que_low.append(i)
                count+=1
    return count

def higher(h):
    visited = [False] * (N + 1)
    que_higher=deque()
    que_higher.append(h)
    visited[h]=True
    count=0
    while que_higher:
        check_higher=que_higher.popleft()
        for i in high[check_higher]:
            if visited[i]==False:
                visited[i]=True
                que_higher.append(i)
                count+=1
    return count

U=higher(X)
if U==0:
    U=1

V=lower(X)
if V==0:
    V=N
else:
    V=N-V

print(U, end=' ')
print(V)
