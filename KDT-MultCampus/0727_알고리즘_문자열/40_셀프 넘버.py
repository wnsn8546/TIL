# https://www.acmicpc.net/problem/4673

N = set(range(1,10001)) # N에 1~1000까지의 수를 저장한다.
generator = set() # 중복되지 않는 생성자 set을 만든다.

for i in range(1, 10001): # 1~10000
    for j in str(i): # i + 각 자리수의 합을 더해 생성자를 찾아 생성자 set에 추가한다.
        i += int(j)
    generator.add(i)

self_number = sorted(N - generator) # 전체 수에서 생성자가있는 숫자를 제외한 셀프넘버를 저장한다.
for i in self_number: # 출력한다.
    print(i)
