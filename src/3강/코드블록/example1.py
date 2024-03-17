from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return i, j

print(twoSum([2,7,11,15], 9))
print(twoSum([3,2,4], 6))

# nums라는 intger의 list와 target이 주어질 때, 
# 다음을 만족하는 a, b를 출력하세요.
# target = nums[a] + nums[b]

# 예시1
# nums = [2, 7, 11, 15], target = 9
# 출력 : 0, 1

# 예시2
# nums = [3, 2, 4]
# 출력 : 1, 2

# 예시3
# nums = [3, 3], target = 6
# 출력 : 0, 1

nums = [2, 7, 11, 15]
nums = [(num, idx) for idx, num in enumerate(nums)]
nums.sort(key=lambda x: x[0])

print(nums)