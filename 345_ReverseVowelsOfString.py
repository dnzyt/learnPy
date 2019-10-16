class Solution:
    def reverseVowels(self, s):
        sl = list(s)
        vowels = 'aeiou'
        i, j = 0, len(s) - 1
        while i < j:
            if sl[i].lower() not in vowels:
                i += 1
            elif sl[j].lower() not in vowels:
                j -= 1
            else:
                sl[i], sl[j] = sl[j], sl[i]
                i += 1
                j -= 1
        return ''.join(sl)
