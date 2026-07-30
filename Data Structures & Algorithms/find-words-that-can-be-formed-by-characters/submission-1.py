class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = Counter(chars)
        res = 0

        for word in words:
            curr_word = defaultdict(int) # by default 0
            good_word = True
            for c in word:
                curr_word[c] += 1
                if c not in count or curr_word[c] > count[c]:
                    good_word = False
                    break
            if good_word:
                res += len(word)
        return res