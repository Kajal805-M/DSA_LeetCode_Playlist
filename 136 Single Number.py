#Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
class Solution(object):
    def singleNumber(self, nums):
        SingleNum=0;   # Initialize the Unique Number
        for i in nums:   # All Element through the loop
            SingleNum^=i;  # concept of XOR
        return SingleNum;

        