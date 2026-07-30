class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        left_prod = 1
        for item in range(len(nums)):
            res[item] = left_prod
            left_prod *= nums[item]
        right_prod = 1
        for item in range(len(nums) - 1, -1, -1):
            res[item] *= right_prod
            right_prod *= nums[item]
        return res