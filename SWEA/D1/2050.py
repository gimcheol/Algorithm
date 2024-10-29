T = input()

for i in T: # T:Hello 일때, 첫번째 char는 H
    answer = ord(i) - 64  # ord() : 문자를 아스키코드로 변환해줌
    print(answer, end=" ")
