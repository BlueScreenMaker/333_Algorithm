import sys
N,M,L=map(int,sys.stdin.readline().split())

rest=list(map(int,sys.stdin.readline().split()))
rest.append(0) # 고속도로 1번째에 휴게소를 세울 수 있으니 0부터 시작
rest.append(L)
rest=sorted(rest)

left=0
right=L

while left<=right:
    mid=(left+right)//2
    count=0
    flag=False
    for i in range(1,len(rest)):
        count+=(rest[i]-rest[i-1]-1)//mid
    if count>M:
        flag=True
    if flag:
        left=mid+1
    else:
        right=mid-1

print(left)