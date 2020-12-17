n=int(input())
position=list(map(int, input().split()))
count=0
for i in range(0,n):
    for j in range(i+1,n):
        if(position[i]==position[j]):
            count = count+1
            break
print(count)