import sys

N=int(sys.stdin.readline())

minus=[]
plus=[]
zero=[]

for i in range(N):
    temp=int(sys.stdin.readline())
    if temp>0:
        plus.append(temp)
    elif temp<0:
        minus.append(temp)
    else:
        zero.append(temp)

minus=sorted(minus, reverse=True)
plus=sorted(plus)


answer=0

while len(minus)>1:
    temp1=minus.pop()
    temp2=minus.pop()
    answer+=temp1*temp2

while len(plus)>1:
    temp3=plus.pop()
    temp4=plus.pop()
    if temp3==1 or temp4==1:
        answer+=temp3+temp4
    else:
        answer+=temp3*temp4

if minus and zero:
    minus.pop()
    zero.pop()

answer+=sum(minus)
answer+=sum(plus)

print(answer)