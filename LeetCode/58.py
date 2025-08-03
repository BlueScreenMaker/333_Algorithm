class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word_list = s.split()
        return len(word_list[-1])

test = Solution()
print(test.lengthOfLastWord("   fly me   to   the moon  "))