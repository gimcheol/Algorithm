n = int(input())

#유클리드 호제법
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

for _ in range(n):
    arr = list(map(int,input().split()))
    k = arr.pop(0)
    sum = 0
    for i in range(k):
        for j in range(k):
            if i<j :
                sum += gcd(arr[i],arr[j])
    print(sum)