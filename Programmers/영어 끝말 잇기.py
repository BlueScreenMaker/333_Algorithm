def solution(n, words):
    answer = []
    flag=len(words)//n
    print(flag)
    slice_list=[]
    for a in range(0,len(words),flag):
        slice_list.append(words[a:a+flag])
    print(slice_list)

    return answer

print(solution(3,["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
