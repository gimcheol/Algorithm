
N = int(input())

N_list = sorted(map(int, input().split()))

M = int(input())

M_list = map(int, input().split())

cnt = {} # 딕셔너리로 키(숫자)와 해당하는 값(등장횟수)를 저장

for num in N_list: # num(숫자)가 N_list안에 몇개있는지
    if num in cnt: # num(숫자)가 cnt안에 있는지, 즉 반복되는지 확인
        cnt[num] += 1
    else:
        cnt[num] = 1

def binarySearch(arr, target, start, end):
    if start > end:
        return 0

    mid = (start + end) // 2
    if arr[mid] == target:
        return cnt.get(target)

    elif target > arr[mid]:
        return binarySearch(arr, target, mid+1, end) #시작값이 mid+1 부터

    else :
        return binarySearch(arr, target, start, mid-1) # 끝값이 mid-1까지

for target in M_list:
    print(binarySearch(N_list, target, 0, len(N_list)-1), end=" ")