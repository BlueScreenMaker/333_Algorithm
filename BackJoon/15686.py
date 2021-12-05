import sys
from itertools import combinations

N,M=map(int,sys.stdin.readline().split())

city=[]
for i in range(N):
    city.append(list(map(int, sys.stdin.readline().split())))

chicken=[]
for i in range(N):
    for j in range(N):
        if city[i][j]==2:
            chicken.append([i,j])

number=len(chicken)
answer=0
mid_answer = sys.maxsize
answer=0
if number==M:
    for q in range(N):
        for p in range(N):
            if city[q][p]==1:
                mid = sys.maxsize
                for t in range(number):
                    nx=abs(q-chicken[t][0])
                    ny=abs(p-chicken[t][1])
                    total=abs(nx+ny)
                    if mid>total:
                        mid=total
                answer+=mid
else:
    count=0
    for candi in list(combinations(chicken, number-M)):
        for x, y in candi:
            city[x][y] = 0
        for a in range(N):
            for b in range(N):
                if city[a][b]==1:
                    temp =sys.maxsize
                    for t in range(number):
                        pX=chicken[t][0]
                        pY=chicken[t][1]
                        if(city[pX][pY]==2):
                            nx = abs(a - pX)
                            ny = abs(b - pY)
                            total = abs(nx + ny)
                            if temp > total:
                                temp = total
                    count+=temp
        if mid_answer>count:
            mid_answer=count
        count=0
        for x, y in candi:
            city[x][y] = 2

if mid_answer!=sys.maxsize:
    answer=mid_answer

print(answer)


