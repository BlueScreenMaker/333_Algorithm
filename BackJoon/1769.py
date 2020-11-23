def Counting(num, count):
    total = 0
    if int(num)>=10:
        temp=list(num)
        for i in range(0,len(temp)):
            total += int(temp[i])
        Counting(str(total),count+1)
    else:
        total=int(num)
        if total%3==0 and total!=0:
            return print(count,"YES",sep='\n')
        else:
            return print(count,"NO",sep='\n')




num=str(input())
Counting(num, 0)