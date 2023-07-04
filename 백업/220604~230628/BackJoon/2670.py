import sys
import decimal

N=int(sys.stdin.readline())
ans=-1
num_list=[]
for a in range(0,N):
    A=float(sys.stdin.readline())
    num_list.append(A)

for a in range(0,N):
    mul=1
    for b in range(a,N):
        mul *= decimal.Decimal(num_list[b])
        if ans < mul:
            ans=mul

print(round(ans,3))
# save_values=[0]*N
# max_valuse=[0]
#
#
# for i in range(0,N-1):
#     save_values.append(decimal.Decimal(num_list[i])*decimal.Decimal(num_list[i+1]))
#     for j in range(i+2,N):
#         save_values.append(decimal.Decimal(save_values[-1]*decimal.Decimal(num_list[j])))
#     # print(save_values)
#     temp1=max(save_values)
#     save_values.clear()
#     save_values.append(round(temp1,3))
# print("".join(map(str, save_values)))