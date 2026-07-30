class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        # 1. Build the frequency array for 'chars'
        # Using a list of size 26 is a standard optimization for lowercase English letters.
        counts = [0] * 26
        for c in chars:
            counts[ord(c) - ord('a')] += 1
            
        res = 0
        
        # 2. Check each word
        for word in words:
            # Create a frequency array for the current word
            word_count = [0] * 26
            is_good = True
            
            for c in word:
                idx = ord(c) - ord('a')
                word_count[idx] += 1
                
                # If word needs more of 'c' than available in 'chars'
                if word_count[idx] > counts[idx]:
                    is_good = False
                    break
            
            # 3. If the word was valid, add its length to the result
            if is_good:
                res += len(word)
                
        return res