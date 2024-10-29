import sys

N, M = map(int, sys.stdin.readline().split())

A = set()
B = set()

name= []

for i in range(N):
    A.add(input())

for i in range(M):
    B.add(input())

for i in A:
    if i in B:
        name.append(i)

print(len(name))
name.sort()
for i in name:
    print(i)