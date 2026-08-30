class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        if len(s) < len(t):
            return ""

        
        need = {}

        for i in t:
            need[i] = need.get(i, 0) + 1
        
        need_count = len(need)
        window = {}
        left = 0
        have = 0
        min_length = float("inf")
        result = [-1, -1]

        for right in range(len(s)):
            char = s[right]

            window[char] = window.get(char, 0) + 1

            if char in need and window[char] == need[char]:
                have += 1
            
            while have == need_count:
                char_left = s[left]

                if (right - left + 1) < min_length:
                    min_length = right - left + 1
                    result = [left,right]
                
                window[char_left] -= 1
                
                if char_left in need and window[char_left] < need[char_left]:
                    have -= 1
                
                left += 1
        
        left, right = result

        if min_length != float("inf"):

            return s[left:right+1]
        else:
            return "" 