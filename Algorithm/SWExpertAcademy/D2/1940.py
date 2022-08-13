import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    result = 0
    velocity = 0
    command_list = []
    for _ in range(N):
        command_list.append(list(map(int, input().split())))
    for i in range(len(command_list)):
        if command_list[i][0] == 0:
            result += velocity
        elif command_list[i][0] == 1:
            velocity += command_list[i][1]
            result +=  velocity
        elif command_list[i][0] == 2:
            if velocity - command_list[i][1] < 0:
                velocity = 0
            else:
                velocity -= command_list[i][1]
            result +=  velocity

    print(f'#{test_case} {result}')