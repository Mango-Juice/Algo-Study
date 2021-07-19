# https://www.acmicpc.net/problem/14717

cards = [] #모든 카드 저장

for i in range(1,11):
    cards.append(i)
    cards.append(i)

yh_score = 0 #영학이 점수
sd_score = 0 #상대방 점수
games = 0 #총 게임 수
win = 0 #이긴 게임 수

yh = input()
first = yh.split()[0]
second = yh.split()[1]

if first == second:
    yh_score = int('1' + first)
else:
    yh_score = (int(first) + int(second)) % 10

#영학이 카드는 카드 더미에서 빼기
cards.remove(int(first))
cards.remove(int(second))

#상대 모든 경우의 수 탐색 및 승리 판정
for i, j in enumerate(cards):
    for k, l in enumerate(cards):
        if i == k:
            break
        if j == l:
            sd_score = 10 + j
        else:
            sd_score = (j + l) % 10
        games += 1
        if sd_score < yh_score:
            win += 1

#반올림
result = str(round(1000*win/games)/1000)

#0의 갯수 맞추기
if len(result) < 5:
    for i in range(len(result),5):
        result = result + '0'

print(result[:5]) #출력
