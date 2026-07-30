class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # create a hashmap save items into it
        # take items out from hashmap 
        # check if hashmap empty
        # if empty it is anagram 
        if len(s) != len(t):
            return False
        hash_set = {}
        for char in s:
            if char not in hash_set:
                hash_set[char] = 1
            else:
                hash_set[char] += 1

        for char in t:
            if char in hash_set:
                hash_set[char] -= 1
            else:
                return False
                       
        for val in hash_set.values():
            if val != 0:
                return False
        return True

        # space complexity -> O(1) (because at max 26 keys for 26 characters)
        # time complexity -> O(N + M)

        # can also do this is one line
        # return Counter(s) == Counter(t)