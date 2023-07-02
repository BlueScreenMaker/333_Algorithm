def solution(name):
    after=[]
    for i in name:
        after.append(min(ord(i)-ord('A'),ord('Z')-ord(i)+1))
    index=0
    ans=0

    while True:
        ans+=after[index]
        after[index]=0
        if sum(after)==0:
            break

        left,right=1,1
        while after[index-left]==0:
            left+=1
        while after[index+right]==0:
            right+=1
        if left<right:
            ans+=left
            index-=left
        else:
            ans+=right
            index+=right
    return ans



print(solution("JEROEN"))