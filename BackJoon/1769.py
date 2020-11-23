def Counting(num, count):
    total = 0
    if int(num)>=10:
        temp=list(num)
        for i in range(0,len(temp)):
            total += int(temp[i])
        Counting(str(total),count+1)
    else:
        total=int(num)
        # total은 이미 위에서 0값으로 설정되어있음
        # num을 기준으로 잡아야하니까 total=num
        if total%3==0 and total!=0:
            return print(count,"YES",sep='\n')
        else:
            return print(count,"NO",sep='\n')

num=str(input())
Counting(num, 0)