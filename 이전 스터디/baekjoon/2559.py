n, k = map(int, input().split())
l = list(map(int, input().split()))

temp_s = sum(l[:k])
print(temp_s)
ans = temp_s

if n == k:
    print(ans)
else:
    for i in range(k, n):
        temp_s = temp_s + l[i]
        temp_s = temp_s - l[i-k]
        if temp_s > ans:
            ans = temp_s
    print(ans)