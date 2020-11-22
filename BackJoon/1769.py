def Counting(num, count):
    temp=list(num)
    total=0
    for i in range (0,len(temp)):
        total += int(temp[i])
    if(total<10):
        if(total==3 or total==6 or total==9):
            return print(count,"YES",sep='\n')
        elif(total==1 or total==2 or total==4 or total==5 or total==7 or total==8):
            return print(count,"NO",sep='\n')
    else:
        count+=1
        Counting(str(total),count)

num=str(input())
Counting(num, 1)