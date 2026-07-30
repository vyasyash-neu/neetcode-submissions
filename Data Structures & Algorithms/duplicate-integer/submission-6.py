class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # if len(nums) != len(set(nums)):
        #     return True
        # return False
        # Space -> O(n)
        # Time -> O(n)

        hash_set = {}
        for num in nums:
            if num in hash_set:
                hash_set[num] += 1
                return True
            else:
                hash_set[num] = 1
        return False
        # Space -> O(n)
        # Time -> O(n)
