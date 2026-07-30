class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # https://www.youtube.com/watch?v=eDmxPfVa81k
        res = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            key = tuple(count)

            if key not in res:
                res[key] = [s]
            else:
                res[key].append(s)
        return list(res.values())