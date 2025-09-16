class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs) == 1:
            return strs[0]
        common=[]
        isCommon=True
        minVal = len(strs[0])
        for str in strs:
            if len(str) < minVal: minVal = len(str)
        for j in range(minVal):
            char = strs[0][j]
            for k in strs:
                if char != k[j]:
                    isCommon=False
                    break
            if isCommon: common+=char
            else: break
        return ''.join(common)
s=Solution()
print(s.longestCommonPrefix(["flower","flow","flight"]))
print(s.longestCommonPrefix(["aa","ab"]))
print(s.longestCommonPrefix(["a"]))
print(s.longestCommonPrefix(["car","cir"]))
