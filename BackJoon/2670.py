import sys


N=int(sys.stdin.readline())

num_list=[]
for a in range(0,N):
    A=float(sys.stdin.readline())
    num_list.append(A)

save_values=[]

for i in range(0,N-1):
    save_values.append(num_list[i])
    for j in range(i+1,N):
        a=save_values[-1]*num_list[j]
        save_values.append(round(a,4))
    print(save_values)
    temp1=max(save_values)
    save_values.clear()
    save_values.append(temp1)
print("".join(map(str, save_values)))