import sys
input = sys.stdin.readline

def check(a: list) -> bool:
    stack = []
    flag = True

    for i in range(len(a)):
        if a[i] == '(' or a[i] == '[': # 여는 애들
            stack.append(a[i])

        else:   # 닫는 애들
            if a[i] ==')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    flag = False
            else:
                if stack and stack[-1] == '[':
                    stack.pop()
                else: flag = False

    if not stack and flag:
        return True
    return False

def cal_string(a: list) -> int:
    stack = []
    for i in range(len(a)):
        if a[i] == '(' or a[i] == '[': # 여는 애들
            stack.append(a[i])

        else: # 닫는 애들
            if a[i] == ')':
                if stack[-1] == '(':
                    stack[-1] = 2
                else:   # 숫자. 올바른 괄호열이기 때문에 '[' 등은 못 들어온다.
                    temp = 0
                    for j in range(len(stack)-1, -1, -1):
                        if stack[j] == '(':
                            stack[-1] = temp * 2
                            break
                        else:   # 그 뒤에 나오는 것도 숫자
                            temp += stack[-1]
                            stack.pop()

            else:   # ']'
                if stack[-1] == '[':
                    stack[-1] = 3
                else:   # 숫자
                    temp = 0
                    for j in range(len(stack)-1, -1, -1):
                        if stack[j] == '[':
                            stack[-1] = temp*3
                            break
                        else:   # 숫자면
                            temp += stack[-1]
                            stack.pop()

    return sum(stack)


a = input().strip()

if check(a):
    print(cal_string(a))
else:
    print(0)

