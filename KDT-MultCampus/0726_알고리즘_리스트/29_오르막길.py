# https://www.acmicpc.net/problem/2846

N = int(input())
height_list = list(map(int, input().split()))
uphill_road_start = height_list[0]
uphill_road_end = 0
uphill_road_length = [0]

for i in range(1, len(height_list)):
    if height_list[i-1] < height_list[i]:
        uphill_road_end = height_list[i]
    else:
        if uphill_road_end - uphill_road_start > 0:
            uphill_road_length.append(uphill_road_end - uphill_road_start)
        if i != len(height_list) - 1:
            uphill_road_start = height_list[i]

if uphill_road_end - uphill_road_start > 0:
    uphill_road_length.append(uphill_road_end - uphill_road_start)

print(max(uphill_road_length))