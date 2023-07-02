num=int(input())
bookDir={}
for i in range (num):
    temp=input()
    if(temp in bookDir.keys()):
        bookDir[temp]=bookDir[temp]+1
    else:
        bookDir[temp]=1

sortBookDir = sorted(bookDir.items())
for i in range (len(sortBookDir)-1,0):
    print(sortBookDir[-1][1])
# print(sortBookDir[-1][0])