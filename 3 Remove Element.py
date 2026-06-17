class Solution(object):
    def removeElement(self, nums, val):
        self=0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[self] = nums[i]
                self += 1
        return self