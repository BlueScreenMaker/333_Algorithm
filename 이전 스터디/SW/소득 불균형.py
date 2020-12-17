N=int(input())
for i in range(0,N):
    length=int(input())
    money_list=list(map(int,input().split()))
    aver=int(sum(money_list)/length)
    sort_money=sorted(money_list)
    count=0
    for j in sort_money:
        if(j<=aver):
            count+=1
        elif(j>aver):
            break
    print(f"#{i+1} {count}")