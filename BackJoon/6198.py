import sys

N=int(sys.stdin.readline())

height=[]
for i in range(N):
    height.append(int(sys.stdin.readline()))

height=height[::-1]

stack=[]

answer=[0 for i in range(N)]

for j in range(N):
    count=0
    while (stack and height[j]>height[stack[-1]]):
        count+=answer[stack.pop()]+1
    stack.append(j)
    answer[j]=count

print(sum(answer))