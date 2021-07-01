import sys

N=int(sys.stdin.readline())

height=[]
for i in range(N):
    height.append(int(sys.stdin.readline()))

stack=[]

answer=0

for j in range(N):
    while(stack and height[j]>=stack[-1]):
        stack.pop()
    stack.append(height[j])
    answer+=len(stack)-1

print(answer)

'''
옥상정원 뒤집어서 생각하기
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
'''