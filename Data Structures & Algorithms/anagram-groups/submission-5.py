class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # s= 3 a =2 
        # hashmap 
        # key -> value 
        ## frequency characters are repeated   --> [word 1, word 2]
        # 1st for loop for all items
        # 2nd for loop for each char in item
        freq = {}
        for word in strs:
            count = [0] * 26
            for char in word:
                alpha = ord(char) - ord('a')
                count[alpha] += 1
            
            # As list is not hashable convert to tuple
            key = tuple(count)

            if key not in freq:
                freq[key] = [word]
            else:
                freq[key].append(word)
            
        return list(freq.values())