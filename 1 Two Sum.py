class Solution(object):
    def twoSum(self, nums, target):
        list={}
        for i in range(len(nums)):
            complement=target-nums[i]
            if complement in list:
                return[list[complement],i]
            list[nums[i]]=i
        