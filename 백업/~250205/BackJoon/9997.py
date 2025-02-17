import sys

N = int(sys.stdin.readline())

words = []
for _ in range(N):
    word = sys.stdin.readline().rstrip()
    standard = 0
    for char in word:
        alpha = ord(char) - ord("a")
        standard |= 1 << alpha
    words.append(standard)

total_alpha = (1 << 26) - 1
answer = 0

def back(count, point):
    global answer
    if count == N-1:
        if point == total_alpha:
            answer += 1
    else:
        back(count+1, point | words[count + 1])
        back(count + 1, point)

back(-1, 0)
print(answer)