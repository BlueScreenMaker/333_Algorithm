def StrPrint(N,count):
    if count==0:
        print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
        return StrPrint(N,count+1)
    elif count>N:
        return print("탈출")
    else:
        hyphen=''
