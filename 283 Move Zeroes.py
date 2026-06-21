class Solution(object):
    def moveZeroes(self, nums):
        temp=0
        for i in range(len(nums)):
            if nums[i]!=0 and nums[temp]==0:
                nums[temp],nums[i]=nums[i],nums[temp]
            if nums[temp]!=0:
                temp+=1
        