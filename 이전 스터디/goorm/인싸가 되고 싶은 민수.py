A,B=map(int,input().split())

if(A-B==0):
    answer=A
    for i in range(2,A+1):
        if(A%i==0):
            answer=i
            break
    print(answer)
else:
    print(2)

# divisor_list=[]
# count_dir={}
#
#
# for i in range(A,B+1):
#     for j in range(2,i+1):
#         if(i%j==0):
#             divisor_list.append(j)
#             if(j*j<i):
#                 divisor_list.append(j)
#
#
#
#
#
#
# for i in divisor_list:
#     try: count_dir[i] += 1
#     except: count_dir[i]=1
#
# sort_dir=sorted(count_dir.items(), key=lambda x: x[1], reverse=True)
#
#
# print(sort_dir[0][0])
#
