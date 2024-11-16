T = int(input())

for x in range(1, T+1):

    memory = input()
    reset_memory ='0'
    change_cnt = 0

    for i in memory:
        if i != reset_memory:
            change_cnt += 1
            reset_memory = i

    print(f'#{x} {change_cnt}')