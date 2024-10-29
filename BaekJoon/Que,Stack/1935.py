N = int(input()) # ABC*+DE/- ==> 123*+45/-
cmd = input()

# 입력된 변수의 값을 저장할 리스트, 초기값은 모두 0으로 설정
N_list = [0]*N

# 변수의 개수만큼 반복하여 각 변수의 값을 입력받고, num_lst에 저장
for i in range(N):
    N_list[i] = int(input())

# 계산을 위해 사용할 스택
stack = []

for i in cmd:
    if 'A' <= i <= 'Z':
        stack.append(N_list[ord(i)-ord('A')])
    # 현재 글자가 연산자라면 스택에서 두 개의 숫자를 꺼냄
    else:
        str2 = stack.pop() # 스택에서 두번째로 들어간 값
        str1 = stack.pop() # 스택에서  첫번째로 들어간 값

        if i == '+':
            stack.append(str1+str2)

        elif i == '-':
            stack.append(str1 - str2)

        elif i == '*':
            stack.append(str1 * str2)

        elif i == '/':
            stack.append(str1 / str2)

# print(stack)
print('{:.2f}'.format(stack[0]))