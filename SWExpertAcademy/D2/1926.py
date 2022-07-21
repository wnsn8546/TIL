n = int(input())

for number in range(1, n+1):
    str_number = str(number)
    cnt = 0

    for i in str_number:
        if i == '3' or i == '6' or i == '9':
            cnt += 1
            
    if cnt > 0:
        for i in range(1, cnt + 1):
            print('-', end = '')
        print('', end = ' ')
    else:
        print(number, end = ' ')