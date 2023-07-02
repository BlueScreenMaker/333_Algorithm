import sys

N = int(sys.stdin.readline())
number_list = list(map(int, sys.stdin.readline().split()))

# 하나만 입력될 경우, 다음 수는 어떤 조건의 수가 와도 됨.
if N==1:
    print("A")

elif N==2:
    if number_list[0]==number_list[1]:
        print(number_list[0])
    # 예제처럼 -1 2 인 경우
    # -1 * -1 + 1
    # -1 * 1 + 3
    # 이 외에도 다른 조건들이 더 올 수 있음
    else :
        print ("A")

else:
    a=0
    if number_list[1]-number_list[0] != 0:
        a=(number_list[2]-number_list[1]) // (number_list[1]-number_list[0])

    b= number_list[1]-number_list[0] * a

    checked = False
    for idx in range(1, N):
        if (number_list[idx] != number_list[idx-1]*a+b):
            checked = True
            break
    if checked:
        print("B")
    else:
        print(number_list[N-1]*a+b)

