N1=int(input())
sequence_list=list(map(int, input().split()))
N2=int(input())
check_list=list(map(int,input().split()))

sort_sequence=sorted(sequence_list)


for a in check_list:
    left = 0
    right = N1 - 1
    flag=False
    while left <= right:
        mid = (left + right) // 2
        if sort_sequence[mid] == a:
            print(1)
            flag=True
            break
        elif sort_sequence[mid] > a:
            right = mid - 1
        else:
            left = mid + 1
    if(flag==False):
        print(0)


            # https://velog.io/@madfinger/Binary-Search%EC%9D%B4%EC%A7%84-%ED%83%90%EC%83%89-%ED%8C%8C%EC%9D%B4%EC%8D%AC