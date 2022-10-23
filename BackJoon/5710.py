import sys

def cacluate_electric(pay, electric):
    if 1 <= pay <= 200:
        electric += pay / 2
    elif 200 < pay <= 29900:
        pay -= 200
        electric = 100 + pay / 3
    elif 29900 <= pay <= 4_979_900:
        pay -= 29900
        electric = 10000 + pay / 5
    else:
        pay -= 4_979_900
        electric = 1_000_000 + pay / 7

    return electric

def check_pay(electric, pay):
    if 1 <= electric <= 100:
        pay += (electric * 2)
    elif 100 <= electric <= 10000:
        electric -= 100
        pay = 200 + (electric) * 3
    elif 10000 < electric <= 1000000:
        electric -= 10000
        pay = 29900 + (electric) * 5
    elif 1000000 < electric:
        electric -= 1_000_000
        pay = 4_97_9900 + (electric) * 7
    return pay

while True:
    A,B = map(int, sys.stdin.readline().split())
    # A = 총 요금
    # B = 이웃과 전기요금 차이
    if A==0 and B==0:
        break

    start = 0
    end = A

    while start <= end:
        mid = (start+end) // 2
        a_electric = cacluate_electric(mid, 0)

        b_electric = cacluate_electric(mid + B, 0)

        sum_electric = a_electric + b_electric
        total_pay = check_pay(sum_electric, 0)

        if A == total_pay:
            print(mid)
            break
        elif A > total_pay:
            start = mid+1
        else:
            end = mid - 1


