class Solution(object):
    def isPalindrome(self,x):
        arr=[]
        new=x
        j=0
        if new<10 and new>=0: return True
        elif new%10==0 or new<0: return False
        for i in range(0,11):
            while new%10!=0 or len(arr)==i and x>=10**i:
                arr.append(new%10)
                new//=10
        for i in reversed(arr):
            if i!=arr[j]:
                return False
            j+=1
        return True