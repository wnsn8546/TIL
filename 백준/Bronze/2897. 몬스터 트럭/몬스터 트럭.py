R, C = map(int, input().split())

parking_map = []
for _ in range(R):
    parking_map.append(input())

broken_list = [0] * 5
for i in range(R-1):
    for j in range(C-1):
        temp = parking_map[i][j] + parking_map[i][j+1] + parking_map[i+1][j] + parking_map[i+1][j+1]
        
        if '#' in temp:
            continue
        else:
            if temp.count('X') == 0:
                broken_list[0] += 1
            elif temp.count('X') == 1:
                broken_list[1] += 1
            elif temp.count('X') == 2:
                broken_list[2] += 1
            elif temp.count('X') == 3:
                broken_list[3] += 1
            elif temp.count('X') == 4:
                broken_list[4] += 1
print(*broken_list, sep='\n')