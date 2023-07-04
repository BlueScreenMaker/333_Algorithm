import re

def solution(files):
    #그룹으로 묶으면 숫자가 살아있어  아니 미치고 환장하겠네 진짜
    #  r'[\d]+'<<이런식으로하면 숫자가 짤려나감;;;
    pattern = r'(\d+)'
    result = []
    for i in files:
        check=re.split(pattern,i)
        result.append(check)
    print(result)
    result=sorted(result,key=lambda x:(x[0].lower(),int(x[1])))

    answer=[]
    for i in result:
        answer.append(''.join(map(str,i)))
    return answer

print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))