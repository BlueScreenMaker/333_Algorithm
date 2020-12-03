N,M=map(int, input().split())
iceberg=[]
for a in range(N):
    iceberg.append(list(map(int, input().split())))

for x in range(0,M):
    for y in range(0,N):
        if iceberg[x][y]!=0:
            if x-1 < -1 or y-1 < -1 or x+1 >= M or y+1 >= N:
                pass
