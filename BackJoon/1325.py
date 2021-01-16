N,M=map(int, input().split())

trust_list=[[] for _ in range(0,N+1)]
for i in range(0,M):
    A,B=map(int,input().split())
    trust_list[B].append(A)

visited=[False] * (N+1)

def Seaching(x):
    for i in trust_list[x]:
        if not visited[i]:
            visited[i] = True
            Seaching(i)


counting_computer={}

for j in range(1,N+1):
    Seaching(j)
    counting_computer[j]=visited.count(True)
    visited=[False]*(N+1)

# print(counting_computer)

sort=sorted(counting_computer.items(), key=lambda x:x[1],reverse=True)

print(sort[0][0],end=' ')
max_count=sort[0][1]
for z in range(1, N):
    if max_count==sort[z][1]:
        print(sort[z][0], end=' ')
    else:
        break