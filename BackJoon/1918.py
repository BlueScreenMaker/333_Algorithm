import sys

operation = sys.stdin.readline().rstrip()

stack = []
answer = ''

# A+B
for cal in operation:
    if cal.isalpha():
        answer += cal
    elif cal == "(":
        stack.append(cal)
    elif cal == "*" or cal == "/":
        while stack and (stack[-1] == "*" or stack[-1] == "/"):
            answer += stack.pop()
        stack.append(cal)
    elif cal == "+" or cal == "-":
        while stack and stack[-1] != "(":
            answer += stack.pop()
        stack.append(cal)
    else:
        while stack and stack[-1] != "(":
            answer += stack.pop()
        stack.pop()

while stack:
    answer += stack.pop()
print(answer)

'''
맘편하게 외우자.
1 알파벳은 걍 출력
2 * 나 / 나오면 우선순위가 높으니 * / 나올때까지 다 꺼내
3 + -는 우선 순위 낮아서 여는 괄호 아니면 다 꺼낸다.
'''