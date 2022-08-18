# 10,000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 증가하는 순서로 출력한다.
# 셀프넘버 : 생성자가 없는숫자.

# gen_list = [0] * 10001

# for i in range(1, 9994):
#     for j in str(i):
#         i += int(j)
#     print(i)    
#     gen_list[i] += 1

# for i in range(1, 9994):
#     if gen_list[i] == 0:
#         print(i)

gen_list = []

for i in range(1, 65):
    for j in str(i):
        i += int(j)   
    gen_list.append(i)

for i in range(1, 65):
    if i not in gen_list:
        print(i)

