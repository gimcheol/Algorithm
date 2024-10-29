import sys

S = sys.stdin.readline()

count = [0] * 26

for i in S:
    if 'a' <= i <= 'z':
        # ord(): 아스키코드로 변환 해주는 함수
        count[ord(i) - ord('a')] += 1

for j in count:
    print(j, end=' ')