import sys
N=int(sys.stdin.readline())

connect=[[] for _ in range(N+1)]
island=[[],['S',0]]

for i in range(2,N+1):
    kind,total,con=map(str,sys.stdin.readline().split(" "))
    island.append([kind,int(total)])
    connect[int(con)].append(i)

def dfs(x):
    count=0
    for check in connect[x]:
        count += dfs(check)
    if island[x][0]=='W':
        count-=island[x][1]
        if count<0: return 0
        else: return count;
    else: return count+island[x][1]


print(dfs(1))
