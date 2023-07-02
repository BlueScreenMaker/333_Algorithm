def gcd(a, b):
    if(b==0):
        return a;
    else:
        return gcd(b,a%b)

def solution(w,h):
    common=gcd(w,h)
    answer=(w*h)-(w+h-common)
    return answer

print(solution(8,12))