def solution(stones, k):
    global niniz
    niniz=0
    left=0
    right=200000000
    global flag
    flag=False
    while left<=right:
        mid=(left+right)//2
        jump_count=k
        for i in stones:
            if i<=mid:
                jump_count-=1
                if jump_count==0:
                    flag=False
                    break
            else:
                jump_count=k
                flag=True
        if flag==True:
            niniz=mid
            left=mid+1
        else:
            right=mid-1
    return niniz+1

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1],3))

'''
def solution(stones, k):
    flag=True
    answer = 0
    while flag:
        counting = 1
        for i in range(0,len(stones)-1):
            if counting<k:
                if stones[i]==0:
                    if stones[i+1]==0:
                        counting+=1
                    else:
                        counting=1
                        pass
                else:
                    stones[i]-=1

            else:
                flag=False
                break
        answer+=1

    return answer-1
'''