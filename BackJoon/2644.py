import sys
from collections import deque

people=int(sys.stdin.readline())

test1, test2=map(int,sys.stdin.readline().split())

total=int(sys.stdin.readline())

relationship=[[] for a in range(0,people+1)]
for b in range(0,total):
    A,B=map(int,sys.stdin.readline().split())
    relationship[A].append(B)
    relationship[B].append(A)

visited=[False for i in range(0,people+1)]

print(relationship)

def familyRelationship(R, V, index):
    que=deque([index])
    visited[index]=True
    while que:
        check1 = que.popleft()
        for p in relationship[check1]:
            if not visited[p]:
                que.append(p)
                visited[p]=True



    return
#
# for i in range(1,people+1):
#     for j in relationship[i]:
#         if j==test1 or j==test2:
#             print(familyRelationship(relationship,visited,i))



