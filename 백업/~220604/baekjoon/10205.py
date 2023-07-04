n = int(input())
num_list=[]
for i in range (0,n):
    num_list.append(list(map(int, input().split())))

for i in range(0,n):
    row_flag=0
    col_flag=1
    for j in range(1, num_list[i][2]+1):
        if(j==num_list[i][2]):
            break;
        elif(row_flag<num_list[i][0]-1):
            row_flag = row_flag + 1
        else:
            col_flag=col_flag+1
            row_flag=0
    print(str(row_flag+1) + str(format(col_flag, '02')))




