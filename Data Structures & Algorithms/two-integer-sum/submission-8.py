class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # # brute-force 2 pointer approach
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if nums[i] + nums[j] == target and i!=j:
        #             return [i, j]
        # # Space -> O(1)
        # # time -> O(n^2)

        # can we do it in O(n)?
        # some_value = target - val 
        hash_map = {} # key -> some_value
                      # value -> index of 
        for index, some_val in enumerate(nums):
            if some_val in hash_map:
                return [hash_map[some_val], index]
            else:
                some_val = target - some_val
                hash_map[some_val] = index

        #Space complexity O(N)
        #time complecity O(N)
