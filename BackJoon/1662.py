string=input()

str_list=[]

length=0
sentence=''

for i in string:
    if i.isdigit():
        length+=1
        sentence=i #5 6 2
    elif i=='(':
        str_list.append((length-1,sentence))
        length=0
    else:
        total, mul=str_list.pop()
        print(total,mul,length)
        length=(int(mul)*length)+total

print(length)