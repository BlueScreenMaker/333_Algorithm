import sys

N, M = map(int, sys.stdin.readline().split())

word_list = []
for i in range(N):
    word_list.append(sys.stdin.readline())

# 26개 다 알고있단 가정
alpha = (1<<27) -1

# 각 단어에 있는 알파벳 정보
info_alpha=[ 0 for _ in range(N)]
for a in range(N):
    word = word_list[a]
    

print(info_alpha)

for a in range(M):
    command, char = map(str,sys.stdin.readline().split())
    if command=='1':
        alpha &= ~(1<<(char-'a'))
    else:
        alpha |= ~(1<<char-'a')




'''
시간 초과
do_not_remember = []
for i in range(M):
    command, alpha=sys.stdin.readline().split()
    if command=='1':
        do_not_remember.append(alpha)
    else:
        do_not_remember.remove(alpha)

    count = 0
    for word in word_list:
        flag=False
        for char in word:
            if char in do_not_remember:
                flag=True
                break
        if not flag:
            count+=1
    print(count)
'''