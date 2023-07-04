N=int(input())

for i in range(0,N):
    order_list = list(map(str, input().split()))
    length=int(order_list[0])*2
    B_number=[]
    O_number=[]
    B_position = 1
    O_position = 1
    turn = 0

    for j in range(1,length,2):
        if(order_list[j]=='B'):
            B_number.append(int(order_list[j+1]))
        else:
            O_number.append(int(order_list[j+1]))

    a=1
    while True:
        push=False
        if(push==False and order_list[a]=='B'):
            if(int(order_list[a+1])==B_position):
                push=True
                B_number.remove(B_position)
                a+=2
                if(a>length):
                    print(f"#{i+1} {turn+1}")
                    break
            elif(int(order_list[a+1])>B_position):
                B_position+=1
            elif(int(order_list[a+1])<B_position):
                B_position-=1

            if O_number:
                if O_position < O_number[0]:
                    O_position+=1
                elif O_position>O_number[0]:
                    O_position-=1

        if(push==False and order_list[a]=='O'):
            if(int(order_list[a+1])==O_position):
                push=True
                O_number.remove(O_position)
                a += 2
                if (a > length):
                    print(f"#{i+1} {turn+1}")
                    break
            elif(int(order_list[a+1])>O_position):
                O_position+=1
            elif(int(order_list[a+1])<O_position):
                O_position-=1
            if B_number:
                if B_position < B_number[0]:
                    B_position += 1
                elif B_position > B_number[0]:
                    B_position -= 1
        turn+=1




