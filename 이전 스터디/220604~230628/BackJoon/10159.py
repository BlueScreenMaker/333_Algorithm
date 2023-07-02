import sys

def check_low(node):
    visited_low[node]=True
    for sub in low[node]:
        if not visited_low[sub]:
            visited_low[sub]=True
            check_low(sub)
    return visited_low

def check_high(node):
    visited_high[node]=True
    for sub in high[node]:
        if not visited_high[sub]:
            visited_high[sub]=True
            check_high(sub)
    return visited_high


N=int(sys.stdin.readline())
M=int(sys.stdin.readline())

low=[[] for _ in range(N+1)]
high=[[] for _ in range(N+1)]

for i in range(M):
    a,b=map(int,sys.stdin.readline().split())
    low[a].append(b)
    high[b].append(a)

for i in range(1,N+1):
    visited_low = [False] * (N + 1)
    visited_high = [False] * (N + 1)
    check_low(i)
    check_high(i)
    result=[ False]* (N+1)
    for j in range(1,N+1):
        if (visited_low[j] or visited_high[j]):
            result[j]=True
        else:
            result[j]=False
    print(result.count(False)-1)


