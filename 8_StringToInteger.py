import re

class Solution:
    def myAtoi(self, str):
        stripS = str.strip()
        if stripS == '' or stripS == '-' or stripS == '+':
            return 0
        s1 = re.match(r'[^\d]+', (stripS.lstrip('-')).lstrip('+'))
        if s1 != None:
            return 0
        else:
            s1 = re.search(r'\-*\+*\d+', stripS).group()
        
        if s1[0:2] == '--' or s1[0:2] == '-+' or s1[0:2] == '++':
            return 0
        res = int(s1)
        if res > 0:
            return 2147483647 if res > 2147483647 else res
        else:
            return -2147483648 if res < -2147483648 else res