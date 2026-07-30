class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for i, number in enumerate(nums):
            complement = target - number
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[number] = i
            