def solution(s):
    length=len(s)//2
    min=len(s)
    pattern=""
    for i in range(1,length+1):
        answer = ""
        count = 1
        pattern=s[:i]
        for j in range(i,len(s), i):
            # print("현재패턴", pattern)
            if(pattern==s[j:i+j]):
                count+=1
            else:
                # print("count", count, "pattern", pattern)
                answer += (count != 1 and str(count) or "")+pattern
                pattern=s[j:i+j]
                count=1
        # print("count", count, "pattern", pattern)
        answer += (count != 1 and str(count) or "")+pattern
        if(min>len(answer)):
            min=len(answer)
        print(min)
    return min

solution("ababcdcdababcdcd")