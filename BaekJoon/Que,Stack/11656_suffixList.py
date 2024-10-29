## 문자열 인덱싱
import sys

S = sys.stdin.readline().strip()

S_list = []

for i in range(len(S)):
    S_list.append(S[i:])

S_list.sort()

for i in S_list:
    print(i)
# import sys
#
# from collections import deque
#
# S = sys.stdin.readline().strip()
#
# S_list = deque()
#
# for i in range(len(S)):
#     S_list.append(S[i:])
#
# S_list.sort()
#
# while S_list:
#     suffix = S_list.pop()
#     print(suffix)