import sys

def checking(node) :
    count[node]=1
    for idx in relation[node]:
        if not count[idx]:
            checking(idx)
            count[node] += count[idx]

N,R,Q=map(int,sys.stdin.readline().split())

relation=[[] for _ in range(N+1)]
count=[ 0 for _ in range(N+1)]

for i in range(N-1):
    a,b=map(int,sys.stdin.readline().split())
    relation[a].append(b)
    relation[b].append(a)

checking(R)

for x in range(Q):
    query=int(sys.stdin.readline())
    print(count[query])