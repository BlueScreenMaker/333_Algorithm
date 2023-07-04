import sys
from collections import deque


N,M=map(int, sys.stdin.readline().split())

heavy=[[]for _ in range(N+1)]
light=[[]for _ in range(N+1)]

for i in range(M):
    a,b=map(int,sys.stdin.readline().split())
    heavy[b].append(a)
    light[a].append(b)

mid=N//2
total=0

def checking_light(index):
    global total
    que=deque()
    visited=[False for _ in range(N+1)]
    que.append(index)
    visited[index]=True
    count=0
    while que:
        check=que.popleft()
        for i in light[check]:
            if not visited[i]:
                visited[i]=True
                count+=1
                if count>mid:
                    total+=1
                    return
                que.append(i)

def checking_heavy(index):
    global total
    que=deque()
    visited=[False for _ in range(N+1)]
    que.append(index)
    visited[index]=True
    count=0
    while que:
        check=que.popleft()
        for i in heavy[check]:
            if not visited[i]:
                visited[i]=True
                count+=1
                if count>mid:
                    total+=1
                    return
                que.append(i)

for v in range(1,N+1):
    checking_heavy(v)
    checking_light(v)

print(total)