from typing import List

class Solution:
    def reverseWords(self, s: List[str]) -> None:
        start, end = 0, len(s) - 1
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        
        index = 0
        start = 0
        while index < len(s):
            if s[index] == ' ' or index == len(s) - 1:
                if s[index] == ' ':
                    end = index - 1
                elif index == len(s) - 1:
                    end = index
                while start < end:
                    s[start], s[end] = s[end], s[start]
                    start += 1
                    end -= 1
                start = index + 1
            
            index += 1