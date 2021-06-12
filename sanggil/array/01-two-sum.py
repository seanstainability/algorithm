from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    # target - n이 있는지 in을 이용하여 탐색
    # for i, n in enumerate(nums):
    #     complement = target - n
    #
    #     if complement in nums[i + 1:]:
    #         return nums.index(n), nums[i + 1:].index(complement) + (i + 1)

    # 첫 번째 수를 뺀 결과 키 조회
    # nums_map = {}
    # # 키와 값을 바꿔서 딕셔너리로 저장
    # for i, num in enumerate(nums):
    #     nums_map[num] = i
    #
    # # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
    # for i, num in enumerate(nums):
    #     if target - num in nums_map and i != nums_map[target - num]:
    #         return nums.index(num), nums_map[target - num]

    # 리팩토링
    nums_map = {}
    # 하나의 for 문으로 통합
    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target - num], i]
        nums_map[num] = i


print(twoSum(nums=[2, 7, 11, 15], target=9))
