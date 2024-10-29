def print_suffixes_sorted(S):
    """
    입력 문자열의 모든 접미사를 찾고 정렬하여 출력하는 함수
    :param S: 입력 문자열
    """
    S_list = []

    for i in range(len(S)):
        S_list.append(S[i:]) # i번째부터 저장, i = 1~S ['baekjoon','aekjoon',... n]

    S_list.sort()

    for suffix in S_list:
        print(suffix)

input_string = "baekjoon"
print_suffixes_sorted(input_string)