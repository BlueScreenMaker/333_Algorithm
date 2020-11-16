import itertools

def solution(nums):
    length=len(nums)
    point=length//2
    catch_list=[]
    for i in nums:
        if not i in catch_list:
            if len(catch_list)<=point-1:
                catch_list.append(i)
            else:
                break;
    # print(catch_list)
    answer = len(catch_list)
    return answer

print(solution([3,1,3,3]))