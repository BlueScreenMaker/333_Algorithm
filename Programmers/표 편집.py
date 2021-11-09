def solution(n, k, cmd):
    answer = ''
    del_info=[False]*n
    del_order=[]
    table=[i for i in range(0,n)]
    cursor=k
    for command in cmd:
        c=command[0]

        if c=="D":
            num=int(command[2])
            if cursor+num<n:
                cursor+=num
            else:
                temp=n-(cursor+num)
                cursor=temp
        elif c=="U":
            num=int(command[2])
            if cursor-num>0:
                cursor-=num
            else:
                temp=n-(cursor-num)
                cursor=temp
        elif c=="C":
            del_info[cursor]=True
            del_order.append(cursor)
            table.remove(cursor)
            length=len(table)-1
            if cursor==length:
                cursor=0
        else:
            check=del_order[-1]
            del_info[check]=False
            table.append(check)
            del del_order[-1]

    for i in del_info:
        if i:
            answer+="X"
        else:
            answer+="O"
    return answer

solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"])