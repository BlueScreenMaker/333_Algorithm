import sys
from collections import deque

N, M, K = map(int, sys.stdin.readline().split(" "))

# 초기 밭의 양분 상태
field = [[5 for _ in range(N)] for _ in range(N)]
# S2D2가 주는 양분 상태
nutrient = []
for i in range(N):
    nutrient.append(list(map(int, sys.stdin.readline().split(" "))))
# 나무 상태 (어린 나무부터 저장 > 어린 나무부터 나이를 먹으니까.)
trees = [[deque() for _ in range(N)] for _ in range(N)]
# 뒤진 나무
dead_trees = [[list() for _ in range(N)] for _ in range(N)]

for a in range(M):
    x, y, z= map(int, sys.stdin.readline().split(" "))
    trees[x-1][y-1].append(z)

# 봄: 자신의 나이만큼 양분을 먹고 나이가 1씩 증가
# 여름: 봄에 죽은 나무가 양분으로 변함 (나이 // 2, 소수점 아래 버림)
def spring_and_summer():
    for i in range(N):
        for j in range(N):
            length = len(trees[i][j]) # 현재 위치의 나무 총 개수 파악
            for k in range(length):
                if field[i][j] < trees[i][j][k]:
                    for _ in range(k, length):
                        temp = trees[i][j].pop()
                        dead_trees[i][j].append(temp)
                    break
                else:
                    field[i][j] -= trees[i][j][k]
                    trees[i][j][k] += 1

        # 죽은 나무 만큼 양분 저장
    for a in range(N):
        for b in range(N):
            while dead_trees[a][b]:
                field[a][b] += dead_trees[a][b].pop() // 2

# 가을: 나무가 번식함.
# 겨울: S2D2가 땅에 양분 채워넣음
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
def fall_and_winter():
    for i in range(N):
        for j in range(N):
            for k in range(len(trees[i][j])):
                # 5의 배수만 번식 가능
                if trees[i][j][k] %5 == 0:
                    for h in range(8):
                        nx = i + dx[h]
                        ny = j + dy[h]
                        if nx < 0 or nx >= N or ny < 0 or ny >= N:
                            continue
                        trees[nx][ny].appendleft(1)
            # 겨울, 양분 추가
            field[i][j] += nutrient[i][j]

for i in range(K):
    spring_and_summer()
    fall_and_winter()

answer = 0
for i in range(N):
    for j in range(N):
        answer += len(trees[i][j])

print(answer)