class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        arr = [[] for i in range(len(nums)+1)]
        for n in nums: 
            # Instead of 
            # count[num] = 1 + count.get(num, 0) 
            # we can do this if else 
            if n in hash:
                hash[n] += 1
            else:
                hash[n] = 1

        for number, count in hash.items(): # key value -> number, count
            arr[count].append(number)

        res = []
        for i in range(len(arr) -1 , 0 , -1):
            for num in arr[i]:
                res.append(num)
                if len(res) == k:
                    return res