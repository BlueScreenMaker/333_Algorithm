def solution(commands):
    answer = []
    table = [[(i,j) for j in range(51)] for i in range(51)]
    # table > [[(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)] ..
    # 표의 인덱스 값을 저장
    values = {(i,j):"" for j in range(51) for i in range(51)}
    # values > (0, 0): "", (1, 0): "", (2, 0): "", (3, 0): "", (4, 0): "", ..
    # 표 값을 저장

    for cmd in commands:
        list_c = list(cmd.split(" "))

        if list_c[0] == "UPDATE":
            # 값 삽입
            if len(list_c) == 4:
                x = int(list_c[1])
                y = int(list_c[2])
                pos = table[x][y]
                values[pos] = list_c[3]
                # values > (1, 1): "menu" ... (1, 2): "category"
            # 값 변경
            else:
                origin = list_c[1]
                change = list_c[2]
                for k, v in values.items():
                    if v == origin:
                        values[k] = change

        elif list_c[0] == "PRINT":
            x = int(list_c[1])
            y = int(list_c[2])
            pos = table[x][y]
            if values[pos] != "":
                answer.append(values[pos])
            else:
                answer.append("EMPTY")

        elif list_c[0] == "MERGE":
            x1 = int(list_c[1])
            y1 = int(list_c[2])
            x2 = int(list_c[3])
            y2 = int(list_c[4])
            pos1 = table[x1][y1]
            pos2 = table[x2][y2]
            if pos1 == pos2:
                continue
            # 값이 있는 셀
            if values[pos1] != "":
                for i in range(51):
                    for j in range(51):
                        # 병합 시켜서 같은 셀로 만들기
                        if table[i][j] == pos2:
                            table[i][j] = pos1
                        #  "MERGE 1 2 1 3" >
                        #  [(1, 0), (1, 1), (1, 2), (1, 2), (1, 4)]
            else:
                for i in range(51):
                    for j in range(51):
                        if table[i][j] == pos1:
                            table[i][j] = pos2
        elif list_c[0] == "UNMERGE":
            x = int(list_c[1])
            y = int(list_c[2])
            pos = table[x][y]
            target = values[pos]
            for i in range(51):
                for j in range(51):
                    if table[i][j] == pos:
                        table[i][j] = (i,j)
                        values[(i,j)] = ""
            values[(x,y)] = target

    return answer

# print(solution(["UPDATE 1 1 menu", "UPDATE 1 2 category", "MERGE 1 2 1 3"]))
print(solution(["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap",
                "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean",
                "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle",
                "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4",
                "PRINT 1 3", "PRINT 1 4"]))
print(solution(["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"]))