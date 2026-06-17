class Solution(object):
    def removeElement(self, nums, value):
        self=0
        for i in range(len(nums)):
            if nums[i] != value:
                nums[self] = nums[i]
                self += 1
        return self