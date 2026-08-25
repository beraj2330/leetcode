class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        left = 0
        count = {}
        max_frequency = 0
        answer = 0

        for right in range(len(s)):

            count[s[right]] = count.get(s[right], 0) + 1

            max_frequency = max(max_frequency, count[s[right]])

            window_size = right - left + 1
            replacements = window_size - max_frequency

            while replacements > k:

                count[s[left]] -= 1
                left += 1

                window_size = right - left + 1
                replacements = window_size - max_frequency
            
            answer = max(answer, right - left + 1)
        
        return answer
        
        