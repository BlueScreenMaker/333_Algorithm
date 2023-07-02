import sys
from collections import deque

people=int(sys.stdin.readline())
test1, test2=map(int,sys.stdin.readline().split())

total=int(sys.stdin.readline())
relationship=[[] for a in range(0,people+1)]
counting=[0]*(people+1)

for b in range(0,total):
    A,B=map(int,sys.stdin.readline().split())
    relationship[A].append(B)
    relationship[B].append(A)


visited=[False for i in range(0,people+1)]


def familyRelationship(t1,t2):
    que=deque([t1])
    visited[t1]=True

    while que:
        check1 = que.popleft()
        visited[check1]=True
        if check1==t2:
            break
        for i in relationship[check1]:
            if not visited[i]:
                que.append(i)
                counting[i]=counting[check1]+1
                visited[i]=True

familyRelationship(test1,test2)

if counting[test2]==0:
    print(-1)
else:
    print(counting[test2])



