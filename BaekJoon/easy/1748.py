# 1 ~ N 까지 수를 이어서 쓰면 다음과 같이 새로운 하나의 수를 얻는다
# 123456789101112....
# 이렇게 만들어진 수의 자릿수를 구하는 프로그램을 작성해라.
# N = 15 이면, 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15



N = int(input())

num_length = 0

for i in range(1, len(N)):
    num_length += 9*(10**i-1)*i

print(num_length)