import sys
sys.setrecursionlimit(10**6)

parent = [[(i,j) for j in range(51)] for i in range(51)]
table = [["EMPTY" for _ in range(51)] for _ in range(51)]
answer = []

def find(r, c):
    if (r, c) == parent[r][c]:
        return parent[r][c]
    pr, pc = parent[r][c]
    parent[r][c] = find(pr, pc)
    return parent[r][c]

def union(r1,c1, r2, c2):
    parent[r2][c2] = parent[r1][c1]

def update_depend_axis(r, c, value):
    pr, pc = find(r, c)
    table[pr][pc] = value

def update_depend_value(before, after):
    for r in range(51):
        for c in range(51):
            pr, pc = find(r, c)
            if table[pr][pc] == before:
                table[pr][pc] = after

def merge(r1, c1, r2, c2):
    r1, c1 = find(r1, c1)
    r2, c2 = find(r2, c2)
    if (r1, c1) == (r2, c2):
        return
    if table[r1][c1] != "EMPTY":
        union(r1, c1, r2, c2)
    else:
        union(r2, c2, r1, c1)

def unmerge(r,c):
    pr,pc = find(r,c)
    value = table[pr][pc]

    temp_list = []
    for x in range(51):
        for y in range(51):
            px, py = find(x, y)
            if (px, py) == (pr, pc):
                temp_list.append((x, y))

    for cx, cy in temp_list:
        parent[cx][cy] = (cx,cy)
        if (cx, cy) == (r,c):
            table[cx][cy] = value
        else:
            table[cx][cy] = "EMPTY"

def print_value(r, c):
    pr, pc = find(r, c)
    answer.append(table[pr][pc])

def solution(commands):
    for command in commands:
        c_list = list(command.split(" "))
        if c_list[0] == "UPDATE":
            if len(c_list) == 4:
                update_depend_axis(int(c_list[1]), int(c_list[2]), c_list[3])
            else:
                update_depend_value(c_list[1], c_list[2])
        elif c_list[0] == "MERGE":
            merge(int(c_list[1]), int(c_list[2]), int(c_list[3]), int(c_list[4]))
        elif c_list[0] == "UNMERGE":
            unmerge(int(c_list[1]), int(c_list[2]))
        else:
            print_value(int(c_list[1]), int(c_list[2]))
    return answer

print(solution(["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean",
                "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle",
                "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle",
                "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4",
                "PRINT 1 3", "PRINT 1 4"]))