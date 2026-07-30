class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hashmap key a=1 c=1 t=1 values-> act,cat
        # return list.values()
        hash_set = {}
        for word in strs:
            count = [0] * 26
            for char in word:
                char_index = ord(char) - ord('a')
                count[char_index] += 1
            tuple_key = tuple(count)                
            if tuple_key in hash_set:
                hash_set[tuple_key].append(word)
            else:
                hash_set[tuple_key] = [word]
        return list(hash_set.values())