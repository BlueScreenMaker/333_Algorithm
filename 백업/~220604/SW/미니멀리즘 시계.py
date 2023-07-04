N=int(input())
time_list=[]
for i in range(0,N):
   time_list.append(int(input()))

count=1
for a in time_list:
    hour=int(a/30)
    temp=a-(hour*30)
    if(temp<0):
        minute=int(a*2)
    else:
        minute=int(temp*2)
    temp=0
    print(f"#{count} {hour} {minute}")
    count+=1