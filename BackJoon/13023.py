import sys
sys.setrecursionlimit(100000)
friendship=[]


def check_relationship(check,R,visited):
    visited[check]=True
    friendship.append(check)
    for i in R[check]:
        if not visited[i]:
            visited[i]=True
            check_relationship(i, R, visited)
            break


people,total=map(int,sys.stdin.readline().split())

relationship=[[]for y in range(0,people)]
for t in range(0,total):
    A,B=map(int,sys.stdin.readline().split())
    relationship[A].append(B)
    relationship[B].append(A)

visited=[False for _ in range(0,people)]

for y in range(0,people):
    if (len(relationship)>0):
        point=y
        break

print(point)
check_relationship(point,relationship,visited)
print(relationship)
print(friendship)
flag=len(friendship)



if flag >= 5:
    print(1)
else:
    print(0)