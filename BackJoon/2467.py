import sys

N=int(sys.stdin.readline())

liquid=list(map(int,sys.stdin.readline().split()))

left=0
right=N-1

check=1000000001*2
answer1=0
answer2=0

while left<right:
    temp=liquid[left]+liquid[right]
    if check>abs(temp):
        check=abs(temp)
        answer1=liquid[left]
        answer2=liquid[right]
        if temp==0:
            break
    if temp<0:
        left+=1
    else :
        right-=1

print(answer1,answer2)

