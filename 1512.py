class solution:
    def identicalPair(self, nums):
        count = 0

        for i in range(len(nums) - 1):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    count += 1
        return count

a = solution()
nums = [1,2,3,1,1,3]
print(a.identicalPair(nums))