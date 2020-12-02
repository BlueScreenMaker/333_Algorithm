N,M=map(int, input().split())

temp_list=[]
for a in range(0,M):
    temp_list.append(list(map(int, input().split())))

trust_list=[[] for _ in range(0,N+1)]
for i in range(0,M):
    trust_list[temp_list[i][1]].append(temp_list[i][0])
print(trust_list)

# trust list에서 가장 길이가 긴 배열을 찾음
#  그 배열을 기준으로 깊이 탐색을 돌리면 될 것 같은데 이론은 잡히는데 구현이 안되니 일단 적어둠
