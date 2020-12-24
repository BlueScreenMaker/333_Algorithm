import sys
sys.setrecursionlimit(100000)
friendship=set()


def check_relationship(check,R,visited):

    # print(check)


    for i in R[check]:
        if not visited[check][i]:
            friendship.add(i)
            print(i)
            check_relationship(i, R, visited)
            break


people,total=map(int,sys.stdin.readline().split())

relationship=[[]for y in range(0,people)]
for t in range(0,total):
    A,B=map(int,sys.stdin.readline().split())
    relationship[A].append(B)
    relationship[B].append(A)

visited=[ [] for _ in range(0,len(relationship))]
for i in range(0,len(relationship)):
    for j in range(0,len(relationship[i])):
        visited[i].append(False)

for y in range(0,people):
    if (len(relationship)>0):
        point=y

# check_relationship(0,relationship,visited)
print(relationship)
print(visited)
# print(friendship)



# if point >= 4:
#     print(1)
# else:
#     print(0)