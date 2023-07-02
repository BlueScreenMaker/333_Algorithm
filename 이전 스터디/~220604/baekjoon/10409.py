task, time= map(int, input().split())
taskList=map(int, input().split())
sum=0;
flag=False;

for i, value in enumerate(taskList):
    sum += value
    if(sum>time):
        print(i)
        flag=True;
        break
    elif(i == task - 1 and flag == False):
        print(task);