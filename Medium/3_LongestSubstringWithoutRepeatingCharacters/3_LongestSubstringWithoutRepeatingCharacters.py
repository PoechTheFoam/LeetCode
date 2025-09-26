class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        r=0
        l=0
        last_seen=dict()
        while r<len(s):
            if s[r] not in last_seen:
                last_seen.update({s[r]:r})
                max_len = max(max_len, r-l+1)
                r+=1
            else:
                l=last_seen[s[r]]+1
                last_seen.update({s[r]:r})
        print(max_len)
        #sliding window
        """
        maxLen=0
        r=0
        l=0
        charset=set()
        while (r<len(s)):
            if (s[r] not in charset):
                charset.add(s[r])
                maxLen = max(maxLen, r - l + 1)
                r+=1
            else:
                while (s[r] in charset):
                    charset.remove(s[l])
                    l+=1
        print(maxLen)"""
solution=Solution()
solution.lengthOfLongestSubstring("pwwkew")
