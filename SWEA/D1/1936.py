N, M = map(str, input().split())

# 1<2, 2<3, 3<1

if N == "3" and M =="2":
    print("A")

elif N == "2" and M == "1":
    print("A")

elif N == "1" and M == "3":
    print("A")

else:
    print("B")