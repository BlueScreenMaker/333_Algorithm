import sys
import heapq

N=int(sys.stdin.readline())

time=[]
end_heap=[]

for i in range(N):
    start,end=map(int,sys.stdin.readline().split())
    time.append([start, end])

time=sorted(time,key=lambda x:x[0])

for j in range(0,len(time)):
    if end_heap:
        if end_heap[0]<=time[j][0]:
            heapq.heappop(end_heap)
        heapq.heappush(end_heap,time[j][1])
    else:
        heapq.heappush(end_heap,time[j][1])

print(len(end_heap))

