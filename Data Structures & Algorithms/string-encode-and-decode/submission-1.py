class Solution:

    def encode(self, strs: List[str]) -> str: #["neet", "code"]
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res # ["4#neet4#code"]

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s): # we need 2 pointers 1 to detect # and second for number of words i.e  4#
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j]) # to slice out exact number
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        return res
