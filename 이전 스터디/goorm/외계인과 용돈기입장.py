N1,N2=map(int, input().split())
money_list=[0]
money_list.extend(list(map(int, input().split())))
section_list=[]
for i in range(0,N2):
    section_list.append(list(map(int, input().split())))

for i in range(1,len(money_list)):
    money_list[i]+=money_list[i-1]


for a in range(0,len(section_list)):
    total=money_list[section_list[a][1]]-money_list[section_list[a][0]-1]
    print('%+d'%total)