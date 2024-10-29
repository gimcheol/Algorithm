N = int(input())

answer = 1

cnt = 0

if N == 0:
    answer = 1

else:
    for i in range(1, N+1):
        answer *= i

while N >=5:
    N //=5
    cnt+=N

print(cnt)

#N = int(input())
#
# cnt = 0
#
# for i in range(5, N + 1, 5):
#     num = i
#     while num % 5 == 0:
#         cnt += 1
#         num //= 5
#
# print(cnt)
