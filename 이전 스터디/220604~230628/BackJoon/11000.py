import sys
import heapq

N=int(sys.stdin.readline())

time=[]
for i in range(N):
    a,b=map(int, sys.stdin.readline().split())
    time.append([a,b])

time=sorted(time, key=lambda x:x[0])

end=[]
heapq.heappush(end,time[0][1])

count=1
for j in range(1,N):
    if end[0] > time[j][0]:
        count+=1
    else:
        heapq.heappop(end)
    heapq.heappush(end,time[j][1])

print(count)