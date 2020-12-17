import sys

upCounting=0
downCounting=0
numCounting=0
spaceCounting=0

for line in sys.stdin:
    for i in line:
        if(65<=ord(i)<=90):
            upCounting+=1
        elif(97<=ord(i)<=122):
            downCounting+=1
        elif(48<=ord(i)<=57):
            numCounting+=1
        elif(ord(i)==32):
            spaceCounting+=1
    print(downCounting,upCounting,numCounting, spaceCounting)
    downCounting=0
    upCounting=0
    numCounting=0
    spaceCounting=0