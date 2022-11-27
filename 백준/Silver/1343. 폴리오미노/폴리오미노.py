from sys import stdin

p1 = 'AAAA'
p2 = 'BB'

board = stdin.readline().replace('\n','')
flag = 0
temp = ''
result = ''

for i in board:
    if i == '.':
        while len(temp) != 0:
            if len(temp) % 2 == 1:
                flag = 1
                print(-1)
                break
            else:
                if len(temp) // 4 > 0:
                    result += 'AAAA' * (len(temp) // 4)
                    temp = temp[4 * (len(temp) // 4):]
                else:
                    result += 'BB' * (len(temp) // 2)
                    temp = ''
        result += '.'     
    else:
        temp += i
    if flag == 1:
        break
else:
    while len(temp) != 0:
        if len(temp) % 2 == 1:
            flag = 1
            print(-1)
            break
        else:
            if len(temp) // 4 > 0:
                result += 'AAAA' * (len(temp) // 4)
                temp = temp[4 * (len(temp) // 4):]
            else:
                result += 'BB' * (len(temp) // 2)
                temp = ''
if flag != 1:
    print(result)