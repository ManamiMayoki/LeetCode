class Solution:
    def romanToInt(self, s: str) -> int:
        roman={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        n=0
        pre_n=0
        for char in reversed(s):
            value=roman[char]
            if value<pre_n:
                n-=value
            else:
                n+=value
            pre_n=value
        return n
            
        