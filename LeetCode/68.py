from typing import List

def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        line_word = []
        # 알파벳 수
        num_letters = 0
        
        for word in words:
            if num_letters + len(line_word) + len(word) > maxWidth:
                total_spaces = maxWidth - num_letters
                gap = len(line_word) - 1
                if gap == 0:
                    line = line_word[0] + ' ' * total_spaces
                else:
                    equal_spaces = total_spaces // gap
                    extra_spaces = total_spaces % gap

                    line = ''
                    for i in range(gap):
                        line += line_word[i]
                        if i < extra_spaces:
                            spaces = equal_spaces + 1
                        else:
                            spaces = equal_spaces
                        
                        line += ' ' * spaces
                    line += line_word[-1]
                result.append(line)
                line_word = []
                num_letters = 0

            line_word.append(word)
            num_letters += len(word)
        
        last_line = ' '.join(line_word)
        last_line += ' ' * (maxWidth - len(last_line))
        result.append(last_line)

        return result