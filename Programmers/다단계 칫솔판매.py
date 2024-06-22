def find(parents, money, seller_id, answer):
    giving = money // 10
    if parents[seller_id] == seller_id or giving == 0:
        answer[seller_id] += money
        return
    mine = money - giving
    answer[seller_id] += mine
    find(parents, giving, parents[seller_id], answer)
    return

def solution(enroll, referral, seller, amount):
    N = len(enroll)
    # 대장 포함
    answer = [0 for _ in range(N+1)]

    p_info = {}
    for i in range(N):
        p_info[enroll[i]] = i+1

    # 초기화: 스스로를 부모로
    parents = [i for i in range(N+1)]
    for i in range(N):
        # 대장이 추천인인 경우
        if referral[i] == "-":
            parents[i+1] = 0
            # 0이 대장임
        else:
            parents[i+1] = p_info[referral[i]]

    for i in range(len(seller)):
        find(parents, amount[i]*100, p_info[seller[i]], answer)

    return answer[1:]

print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
               ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
               ["young", "john", "tod", "emily", "mary"],
               [12, 4, 2, 5, 10]))