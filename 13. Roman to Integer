class Solution:
    def romanToInt(self, s: str) -> int:
        a = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        count = 0
        
        for i in range(len(s) - 1):
            
            if a[s[i]] >= a[s[i+1]]:
                count = count + a[s[i]]
            else:
                count = count - a[s[i]]
        
        count = count + a[s[len(s) - 1]]
        
        return count
