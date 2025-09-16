class Solution(object):
    def isValid(self, s):
        brackets_open=['(','{','[']
        brackets_close=[')','}',']']
        checked=[]
        for i in range(len(s)):
            if s[i] in brackets_open:
                checked.append(s[i])
                print(checked)
            elif s[i] in brackets_close:
                try: brackets_open.index(checked[-1])
                except ValueError: return False
                except IndexError: return False
                if brackets_close.index(s[i])==brackets_open.index(checked[-1]): checked.pop()
                else: return False
                print(checked)
        if not checked: return True
        else: return False

solution = Solution()
print(solution.isValid("()"))