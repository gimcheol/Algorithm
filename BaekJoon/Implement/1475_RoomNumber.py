
N = input() #방번호

card = [0] * 10 # 0~9까지 카드 10개

for i in N:

    if i == '9':
        card[6] +=1

    else:
        card[int(i)] += 1  # card 리스트에서 int(i)에 해당하는 card의 인덱스 1 증가

# 6과 9는 같은 팩으로 사용
card[6] = (card[6] + 1) // 2

max_count = max(card)

print(max_count)