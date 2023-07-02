import sys

people=int(sys.stdin.readline())
totalR=int(sys.stdin.readline())

relationship=[[]for a in range(0,people+1)]

for b in range(0,totalR):
    A, B = map(int, sys.stdin.readline().split())
    relationship[A].append(B)
    relationship[B].append(A)

# print(relationship)
visited=[False]* (people+1)

invite=[]
def check_relationship(check,R,count):
    global visited
    global invite
    visited[check]=True
    if count==2:
        invite.append(check)
        return
    for i in R[check]:
        if not visited[i]:
            visited[i]=True
            invite.append(i)
            check_relationship(i, R,count+1)
            visited[i]=False

check_relationship(1,relationship,0)
print(len(set(invite)))