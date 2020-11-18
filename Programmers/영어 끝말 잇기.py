def solution(n, words):
    answer = []
    flag=len(words)//n
    # print("flag",flag)
    sort_list=[]
    for a in range(0,n):
        for b in range(a,len(words),n):
            sort_list.append(words[b])
    # print(sort_list)
    slice_list=[]
    if(flag*n==len(words)):
        for z in range(0, len(words), flag):
            slice_list.append(sort_list[z:z + flag])
        # print(slice_list)
    else:
        flag+=1
        for z in range(0,len(words),flag):
            slice_list.append(sort_list[z:z + flag])
        # print(slice_list)
    # print(slice_list[2][0])
    point = 0 # 1번 사람 배열 기준점
    go = True
    while go:
        for i in range(1,n):
            # print(len(slice_list[i]))
            for j in range(0,len(slice_list[i])):
                # print("i값",i," j값",j)
                # print(slice_list[0][point],slice_list[i][j])
                if(slice_list[0][point]==slice_list[i][j]):
                    answer.append(i+1)
                    answer.append(j+1)
                    go=False
                    break
        point+=1
        if(point==flag):
            break
    if(go==True):
        for i in range(1,len(words)):
            temp1=words[i-1]
            temp2=words[i]
            if(temp1[-1]!=temp2[0]):
                answer.append((i%n)+1)
                answer.append((sort_list.index(temp2))+1)
                break
    if not answer:
        answer.append(0)
        answer.append(0)



    return answer

print(solution(3,["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))

#

#["hello", "observe", "effect", "take", "either", "recognize","encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]
#