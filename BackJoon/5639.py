import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)
nodes= []

while True:
    try:
        nodes.append(int(input()))
    except:
        break

def check(arr):
    if len(arr) == 0:
        return
    temp_l, temp_r = [], []
    root = arr[0]
    flag = False
    for i in range(1, len(arr)):
        if arr[i] > root:
            temp_l = arr[1:i]
            temp_r = arr[i:]
            flag = True
            break
    if not flag:
        temp_l = arr[1:]

    check(temp_l)
    check(temp_r)
    print(root)

check(nodes)
