K=int(input())
note=[]
for i in range(0,K):
    temp=int(input())
    if(temp!=0):
        note.append(temp)
    else:
        note.pop()

print(sum(note))