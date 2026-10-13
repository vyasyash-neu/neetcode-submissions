class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash_set = {} #key -> char , value -> no of times repeated
        for char in s:
            if char in hash_set:
                hash_set[char] += 1
            else:
                hash_set[char] = 1
        #hash_set = b2 c2
        for char in t:
            if char in hash_set:
                hash_set[char] -= 1
            

        for val in hash_set.values():
            if val != 0:
                return False
        return True