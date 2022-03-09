import sys

N=int(sys.stdin.readline())

house=[]
for i in range(N):
    house.append(list(map(int, sys.stdin.readline().split())))

dp_r=[[0 for _ in range(N)] for _ in range(N)] #가로
dp_c=[[0 for _ in range(N)] for _ in range(N)] #세로
dp_d=[[0 for _ in range(N)] for _ in range(N)] #대각선

dp_r[0][1]=1 # 첫 시작 위치

# 첫 줄은 가로밖에 못놓임
for i in range(2,N):
    if house[0][i]==0:
        dp_r[0][i]=dp_r[0][i-1]

for x in range(1,N):
    for y in range(1,N):
        # 현재 위치 : 대각선 → 가로, 세로, 대각선
        if house[x][y]==0 and house[x][y-1]==0 and house[x-1][y]==0:
            dp_d[x][y]=dp_r[x-1][y-1]+dp_c[x-1][y-1]+dp_d[x-1][y-1]

        if house[x][y]==0:
            # 현재 위치 : 가로 → 가로,세로
            dp_r[x][y]=dp_r[x][y-1]+dp_d[x][y-1]
            #현재 위치 : 세로 → 세로, 가로
            dp_c[x][y]=dp_c[x-1][y]+dp_d[x-1][y]


print(dp_d[N-1][N-1]+dp_c[N-1][N-1]+dp_r[N-1][N-1])
