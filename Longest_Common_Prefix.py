class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        # set return string 
        lcp = ""
        
        # list is empty return lcp
        if len(strs) == 0:
            return lcp
        
        # set minimum length of first list
        minLen = len(strs[0])
        
        # compare and set minimum length in list 
        for i in range(1, len(strs)):
            minLen = min(len(strs[i]), minLen)
            
            
        # compare common character in list
        for i in range(0, minLen):
            current = strs[0][i]
            
            for j in range(0, len(strs)):
                if strs[j][i] != current:
                    return lcp
            
            lcp += current
        
        return lcp
            
        
