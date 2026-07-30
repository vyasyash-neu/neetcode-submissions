class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i, number in enumerate(nums):
            difference = target - nums[i]
            if difference in dict:
                return [dict[difference], i]
            dict[number] = i