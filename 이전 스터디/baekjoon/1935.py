N=int(input())
inputString=list(input())
match={}
cal=[]
flag=65
for i in range(0,N):
    matchingN=int(input())
    match[flag]=matchingN
    flag=flag+1
for a in inputString:
    if 65 <= ord(a) <= 90:
        temp=match.get(ord(a))
        cal.append(temp)
    elif ord(a)==42:
        oper1 = cal.pop()
        oper2 = cal.pop()
        result=oper2*oper1
        cal.append(result)
    elif ord(a)==43:
        oper1 = cal.pop()
        oper2 = cal.pop()
        result = oper2 + oper1
        cal.append(result)
    elif ord(a)==45:
        oper1 = cal.pop()
        oper2 = cal.pop()
        result = oper2 - oper1
        cal.append(result)
    elif ord(a)==47:
        oper1 = cal.pop()
        oper2 = cal.pop()
        result = oper2 / oper1
        cal.append(result)
num="%0.2f" % cal[0]
print(num)