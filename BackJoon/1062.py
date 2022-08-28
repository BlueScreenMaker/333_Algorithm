import sys

N,K = map(int, sys.stdin.readline().split())

result = 0

def dfs(pos, count):
    global result
    if count == K-5:
        learn = 0
        for word in list_word:
            flag = True
            for char in word:
                if not alphabet[ord(char)-ord('a')]:
                    flag=False
                    break
            if flag:
                learn += 1
        result = max(result,learn)

    for x in range(pos,26):
        if not alphabet[x]:
            alphabet[x]=1
            dfs(x, count+1)
            alphabet[x]=0

if K < 5:
    print (0)

elif K == 26:
    print(N)

else:
    list_word = []
    for i in range(N):
        list_word.append(set(sys.stdin.readline().rstrip()))
    alphabet = [ 0 for _ in range(26)]

    essential = ['a','n','t','i','c']
    for char in essential:
        alphabet[ord(char)-ord('a')] = 1
    dfs(0, 0)
    print(result)





