import sys
from collections import deque


def check_relationship(check,R):
    que=deque()
    que.append(check)

    while que:
        point = que.popleft();
        for i in range(0,len(R[point])):
            que.append(i)

        print("음")
    return
people,total=map(int,sys.stdin.readline().split())

relationship=[[]for y in range(0,people)]
for t in range(0,total):
    A,B=map(int,sys.stdin.readline().split())
    relationship[A].append(B)

