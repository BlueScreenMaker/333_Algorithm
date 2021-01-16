import sys
from collections import deque

F,S,G,U,D=map(int,sys.stdin.readline().split())

visited=[False]*(F+U)



def MeetingRoom(position,visited):
    que=deque()
    visited[position]=True
    que.append(position)
    while que:
        check=que.popleft()

        if check>G:
            check-=D
            if (check<=F+U and check>=1):
                if check==G:
                    return
                else:
                    if not visited[check]:
                        visited[check]=True
                        que.append(check)
        elif check<G:
            check+=U
            if (check<=F+U and check>=1):
                if check==G:
                    return
                else:
                    if not visited[check]:
                        visited[check]=True
                        que.append(check)
        elif check==G:
            return


if S==G:
    print(0)
else:
    MeetingRoom(S, visited, 0)
    point=visited.count(True)
    if point==1:
        print("use the stairs")
    else:
        print(point)


