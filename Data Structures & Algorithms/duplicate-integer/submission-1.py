class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash = {}
        for num in nums:
            if num in hash:
                hash[num] += 1
                return True
            else:
                hash[num] = 1
        return False