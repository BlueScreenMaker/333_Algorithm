import itertools
import copy

def calc(operation,seq,exp):
    if exp.isdigit():
        return str(exp)
    else:
        if operation[seq]=="*":
            sub=exp.split("*")
            temp=[]
            for check in sub:
                temp.append(calc(operation,seq+1,check))
            return str(eval("*".join(temp)))
        if operation[seq]=="-":
            sub=exp.split("-")
            temp=[]
            for check in sub:
                temp.append(calc(operation,seq+1,check))
            return str(eval("-".join(temp)))
        if operation[seq]=="+":
            sub=exp.split("+")
            temp=[]
            for check in sub:
                temp.append(calc(operation,seq+1,check))
            return str(eval("+".join(temp)))

def solution(expression, numpy=None):
    answer=0
    operations = [('*', '+', '-'),
                  ('*', '-', '+'),
                  ('+', '-', '*'),
                  ('+', '*', '-'),
                  ('-', '*', '+'),
                  ('-', '+', '*')]

    for oper in operations:
        result = abs(int(calc(oper, 0, expression)))
        if result > answer:
            answer = result

    return answer

print(solution("100-200*300-500+20"))