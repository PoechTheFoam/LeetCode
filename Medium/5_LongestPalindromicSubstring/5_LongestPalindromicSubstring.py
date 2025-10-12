import math


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxlen=0
        output=""
        if len(s)==0 or len(s)==1: return s
        # even length case
        for i in range(len(s)):
            l=i
            r=i+1
            while (l>=0 and r<len(s)) and (s[l]==s[r]):
                l-=1
                r+=1
            if r-l-1>maxlen:
                maxlen=max(maxlen,r-l-1)
                output=s[l+1:r]
                """
                r and l are indices at the end of the search, which always overrune cus it only stops when it does
                overrunning means off by 1 indices compared to actual palindrome's indices
                """
        # odd length case
        for i in range (len(s)):
            l=i-1
            r=i+1
            while (l>=0 and r<len(s)) and (s[l]==s[r]):
                l-=1
                r+=1
            if r - l - 1 > maxlen:
                maxlen = max(maxlen, r - l - 1)
                output = s[l + 1:r]
        return output
solution = Solution()
print(solution.longestPalindrome("abb"))