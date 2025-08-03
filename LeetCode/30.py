from collections import defaultdict
from typing import Counter, List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        word_map = Counter(words)

        result = []

        for i in range(word_len):
            left = i
            right = i
            curr_word_info = defaultdict(int)
            count = 0

            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len

                if word in word_map:
                    curr_word_info[word] += 1
                    count += 1

                    while curr_word_info[word] > word_map[word]:
                        left_word = s[left:left + word_len]
                        curr_word_info[left_word] -= 1
                        left += word_len
                        count -= 1

                    if count == word_count:
                        result.append(left)
                        
                else:
                    curr_word_info = defaultdict(int)
                    count = 0
                    left = right

        return result

    
test = Solution()
print(test.findSubstring("barfoothefoobarman", ["foo","bar"]))