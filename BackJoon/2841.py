import sys

N,P=map(int,sys.stdin.readline().split(" "))

melody=[]
for i in range(N):
    a,b=map(int,sys.stdin.readline().split(" "))
    melody.append([a,b])

stack=[[] for i in range(N+1)]

count=0
for i in range(len(melody)):
    if not stack[melody[i][0]]:
        stack[melody[i][0]].append(melody[i][1])
        count+=1
    else:
        while stack[melody[i][0]] and stack[melody[i][0]][-1]>melody[i][1]:
            stack[melody[i][0]].pop()
            count+=1
        if not melody[i][1] in stack[melody[i][0]]:
            stack[melody[i][0]].append(melody[i][1])
            count+=1

print(count)