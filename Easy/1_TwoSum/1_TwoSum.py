class Solution:
    def twoSum(self,num,target):
        for i in range(len(num)):
            for j in range(i + 1, len(num)):
                output = num[i] + num[j]
                if output == target:
                    output1=[i,j]
                    return output1
        return "Target impossible to add up to"
nums=[2,7,11,15]
target=9