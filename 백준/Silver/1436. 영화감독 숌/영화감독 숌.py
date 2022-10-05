jongmal_list = []

for i in range(3000001):
    if '666' in str(i):
        jongmal_list.append(i)

N = int(input())
print(jongmal_list[N-1])