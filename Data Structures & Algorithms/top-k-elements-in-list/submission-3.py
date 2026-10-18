class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = {} # key (actual value from nums array), 
                           # value(n of times it got occured.)
        frequency_buckets = [[] for i in range(len(nums) + 1)]

        for number in nums:
            frequency_map[number] = 1 + frequency_map.get(number, 0)
        
        for number, count in frequency_map.items():
            frequency_buckets[count].append(number)
        
        res = []
        for i in range(len(frequency_buckets) -1, 0, -1):
            for n in frequency_buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res
