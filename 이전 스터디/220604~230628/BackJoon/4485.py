import heapq
import sys

INF=int(1e9)
dx=[1,-1,0,0]
dy=[0,0,-1,1]

def dij():
    que=[]
    heapq.heappush(que,(0,0,cave[0][0]))
    distance[0][0]=0
    while que:
        px,py,dist=heapq.heappop(que)
        if px==N-1 and py==N-1:
            return distance[px][py]
        for i in range(4):
            nx=px+dx[i]
            ny=py+dy[i]
            if nx<0 or ny<0 or nx>=N or ny>=N: continue
            new_dist = dist + cave[nx][ny]
            if new_dist < distance[nx][ny]:
                distance[nx][ny] = new_dist
                heapq.heappush(que, (nx, ny, new_dist))

count=1
while True:
    N=int(sys.stdin.readline())
    if N==0:
        break
    else:
        cave=[]
        distance=[ [INF for _ in range(N)] for _ in range(N) ]
        for i in range(N):
            cave.append(list(map(int, sys.stdin.readline().split(" "))))
        print(f'Problem {count}: {dij()}')
        count+=1