import sys

while True:
    string=sys.stdin.readline()
    if string=='.':
        break
    else:
        start=[]
        end=[]
        for i in range(len(string)):
            if string[i] == '(':
                start.append(i)
            elif string[i]==')':
                end.append(i)


