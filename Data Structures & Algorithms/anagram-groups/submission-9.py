class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hashMap = {}
        # for word in strs:
        #     key = "".join(sorted(word)) # act
        #     if key not in hashMap:
        #         hashMap[key] = []
        #     hashMap[key].append(word)
        # return list(hashMap.values())
        # m num of words
        # n max length of single word
        # O (m.n) time
        # O(m. nlogn) Space
        ###############################################
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s)
        return list(res.values())