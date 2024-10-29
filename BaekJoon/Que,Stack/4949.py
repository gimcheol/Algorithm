while True:
    s = input()
    if s == ".":
        break

    stack = []
    balanced = True # 괄호의 쌍이 맞는지 확인

    for i in range(len(s)):
        if s[i] == '(' or s[i] == '[':
            stack.append(s[i])

        if s[i] == ')':
            # stack 이 비어있으면 안됨
            if len(stack) == 0:
                balanced = False
                break

            last = stack.pop(-1)
            # stack 이 비어있으면 안됨
            if last != '(':
                balanced = False
                break

        elif s[i] == ']':
            # stack 이 비어있으면 안됨
            if len(stack) == 0:
                balanced = False
                break

            last = stack.pop(-1)
            if last != '[':
                balanced = False
                break

    # 마지막에는 stack이 비어있어야 함.
    if len(stack) !=0:
        balanced = False

    if balanced: # balanced == True
        print('yes')

    else:
        print('no')