class Solution(object):
    def increasingTriplet(self, nums):
        
        smallest = float('inf')
        second_smallest = float('inf')

        for num in nums:
            if num <= smallest:
                smallest = num
            elif num <= second_smallest:
                second_smallest = num
            else:
                return True
        
        return False

solution = Solution()
nums = [1,2,3,4,5]
print(solution.increasingTriplet(nums))