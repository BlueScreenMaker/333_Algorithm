class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_len = len(needle)
        hay_len = len(haystack)
        for i in range(0, hay_len-needle_len):
            sub_word = haystack[i:i+needle_len]
            print(sub_word, i)
            if sub_word == needle:
                return i  
        return -1
    
test = Solution()
print(test.strStr("mississippi", "issi"))