class Solution:
    def isValid(self, s: str) -> bool:
        
        character = {')':'(', '}':'{', ']':'['}
        stack = []
        opening = ['(', '{', '[']
        
        # string length
        length = len(s)
        
        # check for odd length
        if length % 2 != 0:
            return False
        
        for char in s:
            if char in opening:
                stack.append(char)
            else:
                if not stack:
                    return False
                current = stack.pop()
                if char in ')':
                    if current not in character[char]:
                        return False
                if char in '}':
                    if current not in character[char]:
                        return False
                if char in ']':
                    if current not in character[char]:
                        return False
        
        if stack:
            return False
        else:
            return True     
        
                    
