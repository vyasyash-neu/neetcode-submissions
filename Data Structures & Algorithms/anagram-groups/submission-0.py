from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for word in strs:
            sorted_str = "".join(sorted(word))
            anagram_map[sorted_str].append(word)
        return list(anagram_map.values())