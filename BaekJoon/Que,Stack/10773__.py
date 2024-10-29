k = int(input())

stack = []
sum = 0

for i in range(k):

    n = int(input())

    if n != 0:
        stack.append(n)

    elif n == 0:
        stack.pop(-1)

for j in stack:
    sum += j

print(sum)