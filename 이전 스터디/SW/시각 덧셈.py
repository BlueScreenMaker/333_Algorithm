N=int(input())

clock_list=[]


for i in range (0,N):
    clock_list.append(list(map(int, input().split())))

hour=0
minute=0
for a in range(0,N):
    for b in range(0,4):
        if(b%2==0):
            hour+=clock_list[a][b]
        else:
            minute+=clock_list[a][b]
    if(minute>=60):
        temp=int(minute/60)
        hour+=temp
        minute=minute-60
    if(hour>12):
        hour=hour-12

    print('#%d'%(a+1),hour,minute)
    hour=0
    minute=0