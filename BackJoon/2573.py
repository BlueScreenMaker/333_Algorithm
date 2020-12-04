from _collections import deque
import sys

N,M=map(int,sys.stdin.readline().split())
iceberg=[]
iceberg_num=1
for a in range(N):
    iceberg.append(list(map(int, sys.stdin.readline().split())))

year=0
while iceberg_num==1:
    counting_sub=[]
    for x in range(1,N-1):
        for y in range(1,M-1):
            if iceberg[x][y]!=0:
                count=0
                if iceberg[x-1][y]==0:
                    count+=1
                if iceberg[x+1][y]==0:
                    count+=1
                if iceberg[x][y-1]==0:
                    count+=1
                if iceberg[x][y+1]==0:
                    count+=1
                counting_sub.append(count)



    for i in range(1,N-1):
        for j in range(1,M-1):
            if iceberg[i][j]!=0:
                temp=iceberg[i][j]-counting_sub.pop(0)
                if temp<=0:
                    iceberg[i][j]=0
                else:
                    iceberg[i][j]=temp


    visited=[[False for _ in range(0,M)] for _ in range(0,N)]

    for q in range(1,N-1):
        for p in range(1,M-1):
            if iceberg[q][p]!=0:
                visited[q][p]=True

    # print(visited)



    def Check_Iceberg(x,y):
        que=[]
        que.append([x,y])
        while que:
            value=que[0]
            x=value[0]
            y=value[1]
            if visited[x - 1][y] == True:
                visited[x-1][y]=False
                que.append([x-1,y])
            if visited[x + 1][y] == True:
                visited[x + 1][y] = False
                que.append([x+1,y])
            if visited[x][y - 1] == True:
                visited[x][y-1] = False
                que.append([x, y - 1])
            if visited[x][y + 1] == True:
                visited[x][y+1] = False
                que.append([x, y + 1])

            que.pop(0)


    iceberg_num = 0
    for w in range(1,N-1):
        for e in range(1,M-1):
            if iceberg[w][e]!=0 and visited[w][e]==True:
                visited[w][e]=False
                Check_Iceberg(w,e)
                iceberg_num+=1
    year +=1


if iceberg_num==0:
    print(0)
else:
    print(year)

