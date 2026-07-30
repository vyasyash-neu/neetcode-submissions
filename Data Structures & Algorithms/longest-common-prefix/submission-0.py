class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = float('inf') 
        for s in strs:
            if len(s) < min_len:
                min_len = len(s)
        for i in range (0, min_len): # this will iterate over each char
            for j in range (0, len(strs)):# this should go through all strings
                if strs[j][i] != strs[0][i]: # check if j string with ith char is same as first string with ith char
                    return strs[0][:i]
        
        return strs[0][:min_len]