import sys

N=int(sys.stdin.readline())

info=[]

for i in range(N):
    info.append(list(map(int,sys.stdin.readline().split())))

answer=[]
for a in range(0,N):
    k=1
    for b in range(0,N):
        if a!=b:
            if info[a][0]<info[b][0] and info[a][1]<info[b][1]:
                k+=1
    answer.append(k)

print(" ".join(map(str,answer)))