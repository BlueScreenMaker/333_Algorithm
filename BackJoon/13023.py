import sys
sys.setrecursionlimit(100000)
friendship=[]
people,total=map(int,sys.stdin.readline().split())
answer=False
visited=[False for _ in range(0,people)]

def check_relationship(check,R,count):
    global answer
    global visited

    if count>3:
        answer=True
        return
    for i in R[check]:
        if not visited[i]:
            visited[i]=True
            check_relationship(i, R,count+1)
            visited[i]=False


relationship=[[]for y in range(0,people)]
for t in range(0,total):
    A,B=map(int,sys.stdin.readline().split())
    relationship[A].append(B)
    relationship[B].append(A)



for i in range(0,len(relationship)):
    visited[i]=True
    check_relationship(i,relationship,0)
    visited[i]=False
    if answer:
        break

if answer:
    print(1)
else:
    print(0)

# print(relationship)



