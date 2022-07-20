T = int(input())

for test_case in range(1, T + 1):
    n = input()
    
    if n[4:6] == '01' or n[4:6] == '03' or n[4:6] == '05' or n[4:6] == '07' or n[4:6] == '08' or n[4:6] == '10' or n[4:6] == '12':
        if int(n[6:]) <= 31:
            print(f'#{test_case}',n[0:4]+'/'+n[4:6]+'/'+n[6:])
        else:
            print(f'#{test_case}', '-1')
    elif n[4:6] == '4' or n[4:6] == '6' or n[4:6] == '9' or n[4:6] == '11':
        if int(n[6:]) <= 30:
            print(f'#{test_case}',n[0:4]+'/'+n[4:6]+'/'+n[6:])
        else:
            print(f'#{test_case}', '-1')
    elif n[4:6] == '02' :
        if int(n[6:]) <= 28:
            print(f'#{test_case}',n[0:4]+'/'+n[4:6]+'/'+n[6:])
        else:
            print(f'#{test_case}', '-1')
    else:
        print(f'#{test_case}', '-1')
