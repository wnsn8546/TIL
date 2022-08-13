import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    result = 0

    for i in range(len(nums)):
        if nums[i] == max(nums):
            continue
        else:
            for j in range(i, len(nums)):
                if nums[j] == max(nums):
                    result += max(nums) - nums[i]
                    break
                else:
                    if nums[j] == nums[-1] and nums[j] > nums[i]:
                        result += nums[j] - nums[i]
    print(f'#{test_case} {result}')