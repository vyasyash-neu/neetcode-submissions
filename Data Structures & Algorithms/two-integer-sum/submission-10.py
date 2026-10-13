class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hashmap (k,v) -> (target - num), index[num]
        prevMap = {} # val, index
        for i,n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return[prevMap[diff], i]
            prevMap[n] = i
        return