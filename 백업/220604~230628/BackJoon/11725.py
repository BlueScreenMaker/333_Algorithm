import sys
from collections import deque

N=int(sys.stdin.readline())

relationship=[[] for _ in range(N+1)]

parents=[0 for _ in range(N+1)]

for i in range(N-1):
    A,B=map(int,sys.stdin.readline().split())
    relationship[A].append(B)
    relationship[B].append(A)


def searching(idx):
    que=deque()
    que.append(idx)
    while que:
        check=que.pop()
        for node in relationship[check]:
            if parents[node]==0:
                parents[node]=check
                que.append(node)

searching(1)

for i in range(2,N+1):
    print(parents[i])