import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split(" "))

gender = [0 for _ in range(N+1)]
temp = list(sys.stdin.readline().rstrip().split(" "))
for a in range(N):
    if temp[a] == "M":
        gender[a+1] = 0
    else:
        gender[a+1] = 1

relation = []
for b in range(M):
    u, v, d = map(int, sys.stdin.readline().split(" "))
    relation.append([d,u,v])

relation.sort()