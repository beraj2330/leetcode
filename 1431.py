class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        result = []
        maxCandies = max(candies)
        for i in candies:
            if i + extraCandies >= maxCandies:
                result.append(True)
            else:
                result.append(False)
        
        return result


a = Solution()
candies = [2,3,5,1,3]
extraCandies = 3
print(a.kidsWithCandies(candies, extraCandies))