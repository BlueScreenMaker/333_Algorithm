import sys

N=int(sys.stdin.readline())
answer = N**2

coin = []
for i in range(N):
    coin.append(list(sys.stdin.readline().rstrip()))

reverse_coin =[]
for j in coin:
    reverse_coin.append(j[:])

for a in range(N):
    for b in range(N):
        if reverse_coin[a][b]=='T':
            reverse_coin[a][b]='H'
        else:
            reverse_coin[a][b]='T'

for k in range(1 << N):
    temp=[]
    for p in range(N):
        print(f'k {k},  p {p},  k&(1<<p)  {k&(1<<p)}')
        if k & (1<<p):
            temp.append(reverse_coin[p][:])
        else:
            temp.append(coin[p][:])

    count =0
    for q in range(N):
        T_count=0
        for h in range(N):
            if temp[q][h]=='T':
                T_count+=1
        count += min(T_count,N-T_count)
    answer = min(answer, count)
print(answer)