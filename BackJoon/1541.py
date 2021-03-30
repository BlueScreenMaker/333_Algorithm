string=input().split('-')
ans=0

other=[]
first=string[0].split('+')


for a in first:
    ans+=int(a)

for i in range(1,len(string)):
    temp = 0
    split_list=string[i].split('+')
    for j in split_list: #string[i].split('+') 해도 됨. 꼭 리스트 만들 필요 x
        temp+=int(j)
    ans-=temp

print(ans)

