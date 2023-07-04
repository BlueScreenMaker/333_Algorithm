chessList=list(map(int, input().split()))
temp=0
for index, value in enumerate(chessList):
    if(index==0 or index==1):
        temp=1-value
        print(temp, end=' ')
    elif(index==2 or index==3 or index==4):
        temp=2-value
        print(temp, end=' ')
    elif(index==5):
        temp=8-value
        print(temp, end=' ')