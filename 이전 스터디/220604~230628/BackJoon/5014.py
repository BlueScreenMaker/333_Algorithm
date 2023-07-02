import sys
from collections import deque

F,S,G,U,D=map(int,sys.stdin.readline().split())

visited=[False]*(F+1)


def MeetingRoom(position,visited):
    que=deque([[position,0]])
    visited[position]=True
    while que:
        check,count=que.popleft()
        print("층=",check,"횟수=",count)
        if check==G:
            return count
        if check+U<=F and not (visited[check+U]):
                que.append([check+U,count+1])
                visited[check+U]=True
        if check-D>=1 and not (visited[check-D]):
                que.append([check-D,count+1])
                visited[check-D]=True

    return 'use the stairs'

if S==G:
    print(0)
else:
    print(MeetingRoom(S, visited))



# if대신 elif 쓰고
# que에 카운트 삽입대신 더함
