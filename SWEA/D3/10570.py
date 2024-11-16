T = int(input())

for tc in range(1, T+1):

    A, B = input().split()
    cnt = 0

    for i in range(int(A), int(B)+1):
        squared = i ** 0.5

        reversed_num = ''.join(reversed(str(i)))
        reversed_squared = ''.join(str(squared))

        if i == reversed_num and squared * squared == i and reversed_squared == str(squared):
            cnt += 1

    print(f'#{tc} {cnt}')