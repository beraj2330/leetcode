class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        vowel = "aeiou"
        
        left = 0
        count = 0
        max_vowel = 0

        for right in range(len(s)):

            if s[right] in vowel:
                count += 1
            
            if right - left + 1 == k:

                max_vowel = max(max_vowel, count)

                if s[left] in vowel:
                    count -= 1
                
                left += 1
        
        return max_vowel

                

        