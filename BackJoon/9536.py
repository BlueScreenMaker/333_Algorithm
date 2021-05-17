import sys
import re

count=int(sys.stdin.readline())

for i in range(count):
    sound=sys.stdin.readline().split()

    pattern=r'(?P<animal>\w+) (goes) (?P<meowing>\w+)'
    animal_meow=[]
    while True:
        test_case=sys.stdin.readline()
        if test_case.startswith('what'):
            break
        else:
            result=re.match(pattern,test_case)
            animal_meow.append(result.expand('\g<meowing>'))

    ans=[]
    for a in sound:
        if a not in animal_meow:
            ans.append(a)

    print(' '.join(map(str,ans)))
    
