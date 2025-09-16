class Solution(object):
    def romanToInt(self, s):
        x=0
        terms={'I':1,
               "V":5,
               "X":10,
               "L":50,
               "C":100,
               "D":500,
               "M":1000,}
        for i in range (len(s)):
            base=terms.get(s[i])
            if i<len(s)-1 and base<terms.get(s[(i+1)]): x-=base
            else: x+=base
        return x

solution = Solution()
print(solution.romanToInt("III"))

