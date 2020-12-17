import math
N, T=map(int, input().split())
bus_list=[]
for i in range(0,N):
    bus_list.append(list(map(int, input().split())))

result={}

for i in range(0,len(bus_list)):
    flag=False
    if(T==bus_list[i][0]):
        print(i+1)
        flag=True
        break
    elif(T>bus_list[i][0]):
        temp = (T - bus_list[i][0]) / bus_list[i][1]
        count = math.ceil(temp)
        result.setdefault(i + 1, (bus_list[i][0] + (bus_list[i][1] * count)) - T)
    elif(T<bus_list[i][0]):
        result.setdefault(i+1,bus_list[i][0]-T)
if(flag==False):
    sort_r=sorted(result.items(),key=lambda t : t[1])
    print(sort_r[0][0])
