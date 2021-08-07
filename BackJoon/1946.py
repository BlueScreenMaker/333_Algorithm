import sys

T=int(sys.stdin.readline())
for i in range(T):
    N=int(sys.stdin.readline())
    rank=[]
    checking=[]
    for j in range(N):
        a,b=map(int,sys.stdin.readline().split())
        rank.append([a,b])

    rank=sorted(rank, key=lambda x:x[0])
    checking.append(rank[0][1])
    total=1

    for z in range(1,N-1):
        point=checking[-1]
        if point>=rank[z][1]:
            total+=1
            checking.append(rank[z][1])
        else:
            continue
    print(total)