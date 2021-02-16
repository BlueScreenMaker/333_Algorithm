NOTATION='0123456789ABCDEF'

def numeral_system(number,base):
    q,r=divmod(number,base)
    n=NOTATION[r]
    return numeral_system(q,base)+n if q else n

def list_chunk(lst,n):
    return [lst[i:i+n] for i in range(0,len(lst),n)]

def solution(n, t, m, p):
    number=[]
    count=0
    while len(number)<m*t:
        temp=list(numeral_system(count,n))
        for i in temp:
            number.append(i)
        count+=1
    test=list_chunk(number,m)
    answer = ''
    for a in range(0,len(test)):
        for b in range(0,m):
            if(len(answer)<t and b==p-1):
                answer+=test[a][b]

    return answer


print(solution(16,16,2,1))