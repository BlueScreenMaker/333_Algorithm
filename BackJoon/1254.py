import sys

string=list(sys.stdin.readline().rstrip())

length=len(string)
total=length

for i in range(length):
    temp=string[i:]
    if temp==temp[::-1]:
        total+=i
        break

print(total)