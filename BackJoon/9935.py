import sys

from pip._vendor.progress.counter import Stack

N=int(sys.stdin.readline())

number_ticket=list(map(int, sys.stdin.readline().split()))

line=[]
temp=Stack()

count=1
flag=True


for i in number_ticket:
    if i!=count:
        if not temp:
            check=temp.peek()
            if(check==count):
                line.append(temp.pop())
                count+=1
            else:
                temp.append(i)
        else:
            temp.append(i)
    else:
        line.append(i)
        count+=1

print(line,temp)