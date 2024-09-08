class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #length of nums
        n = len(nums)
        result = [1] * n

        left_product = 1
        for i in range(n):
            result[i] = left_product
            left_product *= nums[i]
        
        right_product = 1
        for j in range(n-1, -1, -1):
            result[j] *= right_product
            right_product *= nums[j]
        
        return result

solution = Solution()
nums = [1,2,3,4]
print(solution.productExceptSelf(nums))