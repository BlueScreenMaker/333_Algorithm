def solution(record):
    user={}
    uid=[]
    answer=[]
    for i in record:
        save_word=list(i.split(' '))
        # print(save_word)
        if save_word[0]=='Enter':
            user[save_word[1]]=save_word[-1]
        elif save_word[0]=='Leave':
            uid.append(save_word[1])
        elif save_word[0]=='Change':
            user[save_word[1]]=save_word[-1]
    for j in record:
        print_word=list(j.split(' '))
        if print_word[0]=='Enter':
            answer.append(f"{user[print_word[1]]}님이 들어왔습니다.")
        elif print_word[0]=='Leave':
            answer.append(f"{user[print_word[1]]}님이 나갔습니다.")
    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))