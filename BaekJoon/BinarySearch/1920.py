import sys
# N: A의 자연수의 갯수
N = int(sys.stdin.readline())
# A: N개 배열 , 여기서 arr에 들어있는 수들이 몇개인지 알아내야함
A = list(map(int, sys.stdin.readline().split()))
# M: arr의 갯수
M = int(sys.stdin.readline())
# arr: M개 배열
arr = list(map(int, sys.stdin.readline().split()))

A.sort() # A배열 정렬해야 찾는다

for num in arr: # num : 찾아야할 숫자
    left, right = 0, N-1
    Search = False # 찾았는지 여부를 저장하는 변수,
                    # 처음에는 아직 찾지 않았으니까 Falase
    while left <= right: #
        mid = (left+right) // 2 # 중간값
        if num == A[mid]: # 중간값과 찾으려는 값이 같으면
            Search = True # 찾았다고 표시
            print(1)
            break # 값을 찾았으니까 반복문 탈출
        elif num > A[mid]: # 찾으려는 값이 중간값보다 크면
            lt = mid + 1 # 왼쪽 범위를 중간값보다 오른쪽으로 옮김
        else: # 찾으려는 값이 중간값보다 작다면
            rt = mid - 1 # 오른쪽 범위를 중간값보다 왼쪽으로 옮김

    if not Search: # 값을 못찾는 경우
        print(0)


# 시간초과 해결
# N: A의 자연수의 갯수
# N = int(input())
# # A: N개 배열 , 여기서 arr에 들어있는 수들이 몇개인지 알아내야함
# A = sorted(map(int, input().split()))
# # M: arr의 갯수
# M = int(input())
# # arr: M개 배열
# arr = map(int, input().split())
#
# # 결과를 저장할 리스트
# result = []
#
# for num in arr:  # num : 찾아야할 숫자
#     left, right = 0, N - 1
#     found = False  # 찾았는지 여부를 저장하는 변수, 처음에는 아직 찾지 않았으니까 False
#     while left <= right:
#         mid = (left + right) // 2
#         if num == A[mid]:
#             found = True
#             result.append(1)
#             break
#         elif num > A[mid]:
#             left = mid + 1
#         else:
#             right = mid - 1
#
#     if not found:
#         result.append(0)
#
# # 결과 출력
# for r in result:
#     print(r)
