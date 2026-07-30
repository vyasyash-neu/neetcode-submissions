class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hash_s = {}
        for char in s:
            hash_s[char] = hash_s.get(char, 0) + 1
        for char in t:
            if char not in hash_s or hash_s[char] == 0:
                return False
            hash_s[char] -= 1

        return True