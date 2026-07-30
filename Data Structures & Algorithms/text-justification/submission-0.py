class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        curr_length = 0 # only for word count in the line
        i = 0 # for iteration
        line = []
        res = []
        # new_word = words[i]
        while i < len(words):
            if curr_length + len(line) + len(words[i]) <= maxWidth:
                line.append(words[i])
                curr_length = curr_length + len(words[i])
                i += 1
            else:
                extra_spaces = maxWidth - curr_length
                num_of_gaps = len(line) - 1 # no space before first word
                if num_of_gaps == 0:
                    trail_space = maxWidth - len(line[0])
                    res.append(line[0] + " " * trail_space)
                else:
                    gap_index = 0
                    space = extra_spaces // max(1, num_of_gaps) # for event spaces
                    remainder = extra_spaces % num_of_gaps # for odd space we have to add 1 space extra                
                    while gap_index < num_of_gaps:  ## Once the word is added we have to add the gaps
                        line[gap_index] += " " * space      # always
                        if gap_index < remainder:
                            line[gap_index] += " "
                        gap_index += 1
                    res.append("".join(line))
                curr_length = 0
                line = []
        last_line = " ".join(line)
        trail_space = maxWidth - len(last_line)
        res.append(last_line + (" " *trail_space))
        return res