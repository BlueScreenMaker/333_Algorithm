import sys

N=int(sys.stdin.readline())

time_list=[]

count=1
ans=0

for i in range(0,N):
    time_list.append(list(map(int, sys.stdin.readline().split())))

time_list=sorted(time_list,key=lambda x:(x[1],x[0]))
print(time_list)
check=time_list[0][1]
for i in range(1,N):
    if(check<=time_list[i][0]):
        count+=1
        print(check,count)
        check=time_list[i][1]
print(count)

# time_list=sorted(time_list, key=lambda x:(x[0],x[1]))
# print(time_list)

# check = time_list[0][1]
# for j in range(1, N):
#     print("time값", time_list[j][0])
#     if (check <= time_list[j][0]):
#         print(j,check)
#         ans += 1
#         check = time_list[j][1]
# for i in range(0,N):
#     check=time_list[i][1]
#     for j in range(i,N):
#         if(check<=time_list[j][0]):
#             count+=1
#             check=time_list[j][1]
#     if ans<count:
#         ans=count
#     count = 0
# print(ans+1)

