card_length=int(input())
card_list=list(map(int, input().split()))

check_length=int(input())
check_list=list(map(int, input().split()))

card_list.sort()

for i in check_list:
    left=0
    right=card_length-1
    flag=False
    while left<=right:
        mid = (left+right) // 2
        if (i==card_list[mid]):
            print(1,end=' ')
            flag=True
            break
        elif i<card_list[mid]:
            right=mid-1
        else:
            left=mid+1
    if(flag==False):
        print(0, end=' ')
