class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frez_map = {}
        for num in nums:
            if num in frez_map:
                frez_map[num] += 1
            else:
                frez_map[num] = 1
        sorted_items = sorted(frez_map.items(), key= lambda x:x[1], reverse = True)
        # x:x[1] because frez_map.items will have [0,1] element which will be key,value we want to sort on the basis of values
        # sort reverse true becuase we want descending elements at the top
        result = []
        for i in range(k):
            result.append(sorted_items[i][0])
        return result
