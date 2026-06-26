class Solution(object):
    def maxProduct(self, nums):

        max_prod = nums[0]
        min_prod = nums[0]
        ans = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            if num < 0:
                max_prod, min_prod = min_prod, max_prod

            max_prod = max(num, max_prod * num)
            min_prod = min(num, min_prod * num)

            ans = max(ans, max_prod)

        return ans