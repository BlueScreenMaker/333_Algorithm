case=input()
list21=[] #21 위치저장
list12=[] #12 위치저장
flag=False
for i in range(0,len(case)-1):
    temp=case[i:i+2]
    if(temp=='21'):
        list21.append(i)
    elif(temp=='12'):
        list12.append(i)
for a in list12:
    for b in list21:
        if(abs(a-b)!=1):
            flag=True

if(flag==False):
    print("No")
else:
    print("Yes")



# for i in range(0,len(case),2):
#     if(len(case)%2==0):
#         split_list.append(case[i:i+2])
#     else:
#         print()
#     # try:
#     #     split_list.append(case[i:i+2])
#     # except IndexError:
#     #     split_list.append(case[i])
#
# for value in split_list:
#     if(value=='12'):
#         flag1=True
#     elif(value=='21'):
#         flag2=True
#
# if(flag1==True and flag2==True):
#     print("Yes")
# else:
#     print("No")