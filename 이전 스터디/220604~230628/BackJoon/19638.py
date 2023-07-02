import heapq
import sys

N,H,T=map(int,sys.stdin.readline().split())

height=[]
for i in range(N):
    heapq.heappush(height,-(int(sys.stdin.readline())))

count=0

for j in range(T):
    magic=heapq.heappop(height)*-1
    if magic==1:
        heapq.heappush(height,-1)
    elif magic<H:
        heapq.heappush(height,magic*-1)
        break
    else:
        heapq.heappush(height,(magic//2)*-1)
        count+=1

final=heapq.heappop(height)*(-1)
if final>=H:
    print("NO")
    print(final)
else:
    print("YES")
    print(count)
