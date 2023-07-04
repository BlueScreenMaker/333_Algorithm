import sys

N,K=map(int,sys.stdin.readline().split())

type_coin=[]
for i in range(N):
    type_coin.append(int(sys.stdin.readline()))

money=K
count=0
for j in range(N-1,-1,-1):
    count+=money//type_coin[j]
    money%=type_coin[j]
    if(money==0):
        break

print(count)
