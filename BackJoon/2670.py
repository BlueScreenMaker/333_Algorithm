import sys

N=int(sys.stdin.readline())

num_list=[]
for a in range(0,N):
    num_list.append(list(map(int, sys.stdin.readline().split())))

save_values=[0]*(N*N)

for i in range(0,N):
    for j in range(i,N):
        print()