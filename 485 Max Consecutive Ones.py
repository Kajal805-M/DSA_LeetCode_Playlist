#Given a binary array nums, return the maximum number of consecutive 1's in the array.
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        a=0
        b=0
        for i in nums:
            if i==0:
                if a>b:
                    b=a
                a=0
            else:
                a+=1
        return max(a,b) 