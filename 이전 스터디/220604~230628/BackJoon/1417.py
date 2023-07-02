import sys

N=int(sys.stdin.readline())

vote=[]
for i in range(N):
    vote.append(int(sys.stdin.readline()))

count=0
som=vote[0]
other=sorted(vote[1:],reverse=True)

if N==1:
    print(count)
else:
    while som<=other[0]:
        som+=1
        other[0]-=1
        count+=1
        other=sorted(other,reverse=True)

    print(count)