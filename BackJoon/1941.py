import sys

dx = [-1,1,0,0]
dy = [0,0,-1,1]

class_site = []
for i in range(5):
    class_site.append(list(sys.stdin.readline().strip()))

visited = [[False for _ in range(5)] for _ in range(5)]

def dfs (pick, S, Y):
    if Y > 3:
        return
    if len(pick)==7 and S >=4 :
        pick = tuple(sorted(pick))

def searching(px,py, total, Scount):
    visited[px][py]=True
    for i in range(4):
        nx = px+dx[i]
        ny = py+dy[i]
        if nx < 0 or ny < 0 or nx >= 5 or ny >= 5: continue
        if not visited[nx][ny]:
            if total==5:
                return Scount
            else:
                if class_site[nx][ny]=='S':
                    visited[nx][ny]=True
                    searching(nx,ny,total+1, Scount+1)
                    visited[nx][ny] = False

                else:
                    visited[nx][ny]=True
                    searching(nx, ny, total + 1, Scount)
                    visited[nx][ny] = False

print(searching(0,0,0,0))
