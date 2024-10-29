def infix_to_postfix(expression):
    # 스택과 후위 표기식을 저장할 변수를 초기화합니다.
    stack = []
    postfix = ''

    # 표현식을 한 문자씩 반복합니다.
    for char in expression:
        # 알파벳인 경우에는 그대로 결과에 추가합니다.
        if char.isalpha():
            postfix += char
        else:
            # 연산자인 경우에는 처리를 합니다.
            if char == '(':
                # '('이면 스택에 넣습니다.
                stack.append(char)
            elif char == '*' or char == '/':
                # '*' 또는 '/'이면, 스택에서 '*' 또는 '/'가 나올 때까지 pop하여 결과에 추가한 후 현재 연산자를 스택에 넣습니다.
                while stack and (stack[-1] == '*' or stack[-1] == '/'):
                    postfix += stack.pop()
                stack.append(char)
            elif char == '+' or char == '-':
                # '+' 또는 '-'이면, 스택에서 '('를 만날 때까지 pop하여 결과에 추가한 후 현재 연산자를 스택에 넣습니다.
                while stack and stack[-1] != '(':
                    postfix += stack.pop()
                stack.append(char)
            elif char == ')':
                # ')'이면, 스택에서 '('를 만날 때까지 pop하여 결과에 추가한 후 '('를 스택에서 제거합니다.
                while stack and stack[-1] != '(':
                    postfix += stack.pop()
                stack.pop()

    # 스택에 남은 모든 연산자를 결과에 추가합니다.
    while stack:
        postfix += stack.pop()

    return postfix


# 사용자로부터 중위 표기식을 입력 받습니다.
expression = input().strip()

# 중위 표기식을 후위 표기식으로 변환합니다.
postfix_expression = infix_to_postfix(expression)

# 후위 표기식을 출력합니다.
print(postfix_expression)
