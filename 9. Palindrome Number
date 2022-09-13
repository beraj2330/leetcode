class Solution(object):
    def isPalindrome(self, x):
        
        if x<0:
            return False
        count=0
        value = x
        
        
        while(x!=0):
            remainder = x % 10
            count = count*10 + remainder
            x = x//10
        
        if count == value:
            return True
        else:
            return False
        
if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome(121))
