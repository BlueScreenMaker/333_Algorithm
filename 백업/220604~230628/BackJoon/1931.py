import sys

N=int(sys.stdin.readline())

time_list=[]

count=1

for i in range(0,N):
    time_list.append(list(map(int, sys.stdin.readline().split())))

time_list=sorted(time_list,key=lambda x:(x[1],x[0]))

check=time_list[0][1]
for i in range(1,N):
    if(check<=time_list[i][0]):
        count+=1
        check=time_list[i][1]
print(count)


