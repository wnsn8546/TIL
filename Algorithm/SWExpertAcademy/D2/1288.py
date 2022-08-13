T = int(input())

for test_case in range(1, T + 1):
    n = input()
    my_dict = {}
    number = n
    cnt = 1

    while True:
        for i in number:
            if i in my_dict:
                my_dict[int(i)] += 1
            else:
                my_dict[int(i)] = 1
        
        if (0 in my_dict) and (1 in my_dict) and (2 in my_dict) and (3 in my_dict) and (4 in my_dict) and (5 in my_dict) and (6 in my_dict) and (7 in my_dict) and (8 in my_dict) and (9 in my_dict):
            print(f'#{test_case}', number)
            break
        
        cnt += 1
        number = str(int(n) * cnt)