class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        position = 0
        
        if target in nums:
            for i in range(len(nums)):
                if nums[i] == target:
                    return i 
        else:
            for i in range(len(nums)):
                if nums[i] > target:
                    return i
            return len(nums)
