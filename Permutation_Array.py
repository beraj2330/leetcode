class Permutation:
    
    def per(self, nums):
        result = []

        for i in range(0,len(nums)):
            result.append(nums[nums[i]])

        return result


a = Permutation()

list = [0,2,1,5,3,4]
print(a.per(list))
