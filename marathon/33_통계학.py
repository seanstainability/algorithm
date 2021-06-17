# https://www.acmicpc.net/problem/2108
# 산술평균 : N개의 수들의 합을 N으로 나눈 값
# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값
# 범위 : N개의 수들 중 최댓값과 최솟값의 차이
# 첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.
# 둘째 줄에는 중앙값을 출력한다.
# 셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.
# 넷째 줄에는 범위를 출력한다.

import sys
from collections import Counter

n = int(sys.stdin.readline())
nums = []
for i in range(n):
    nums.append(int(sys.stdin.readline()))
nums.sort()

print(round(sum(nums) / n)) # 산술평균

print(nums[n // 2]) # 중앙값

nums_s = Counter(nums).most_common() # 최빈값
if len(nums_s) > 1:
    if nums_s[0][1] == nums_s[1][1]: # 가장 빈도수 높은 상위 2개가 같을 경우
        print(nums_s[1][0]) # 두 번째로 작은 값(오름차순이므로)
    else:
        print(nums_s[0][0])
else:
    print(nums_s[0][0])

print(nums[-1] - nums[0]) # 범위
