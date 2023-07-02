import sys
import re

count=int(sys.stdin.readline())

for i in range(count):
    sound=sys.stdin.readline().split()

    pattern=r'(?P<animal>\w+) (goes) (?P<meowing>\w+)'
    animal_meow=[]
    while True:
        test_case=sys.stdin.readline()
        if test_case=='what does the fox say?\n':
            break
        else:
            result=re.match(pattern,test_case)
            animal_meow.append(result.expand('\g<meowing>'))

    check='['
    for j in range(0,len(animal_meow)):
        if j!=len(animal_meow)-1:
            check+=animal_meow[j]+"|"
        else:
            check+=animal_meow[j] + ']'
    answer=''
    for z in sound:
        answer+=re.sub(check,'',z)
    print(answer)
    # ans=[]
    # for a in sound:
    #     if a not in animal_meow:
    #         ans.append(a)
    #
    # print(' '.join(map(str,ans)))

