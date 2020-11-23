def solution(n, words):
    answer = [0,0]
    length=len(words)
    for i in range(1,length):
        if( words[i-1][-1]!=words[i][0] or words[i] in words[:i]):
            answer[0]=(i%n)+1
            answer[1]=(i//n)+1
            break

    return answer

print(solution(3,["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))

