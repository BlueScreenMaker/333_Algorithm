def solution(a):
    answer = 2 # 무조건 일단 양 끝은 살아남음
    N = len(a)

    if 0<=N<=2:
        # 풍선의 개수가 0,1,2개는 일단 생존 다 가능
        return N
    left=a[0]
    right=a[-1]

    for i in range(1,N):
        if left>a[i]:
            answer+=1
            left=a[i]
        if right>a[N-1-i]:
            answer+=1
            right=a[N-1-i]

    if left==right:
        answer-=1

    return answer

print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))