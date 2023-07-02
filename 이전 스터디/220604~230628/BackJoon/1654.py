N, K=map(int, input().split())

LAN=[]

for i in range (0,N):
    LAN.append(int(input()))

left=1
right=max(LAN)

while left<=right:
    mid=(left+right)//2
    total=0
    for i in LAN:
        total+=i//mid
    if total>=K:
        left=mid+1
    else:
        right=mid-1
print(right)
