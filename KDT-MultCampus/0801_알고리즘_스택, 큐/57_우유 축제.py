# https://www.acmicpc.net/problem/14720

N = int(input())
milk_stores = list(map(int, input().split()))# 우유가게리스트
nyam = 0 # 마지막으로 먹은 우유의 맛을 저장. 0-딸기 1-초코 2-바닐라
result = 0 # 총 몇개를 먹었는지 더해서 출력할 변수

for i in range(0, len(milk_stores)):
    if milk_stores[i] == nyam:
        nyam = (nyam + 1) % 3
        result += 1
print(result)