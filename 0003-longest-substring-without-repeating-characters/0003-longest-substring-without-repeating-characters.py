class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_next_index = {}
        ans = 0
        left = 0 
        for right, char in enumerate(s):  
            if char in char_next_index and char_next_index[char] > left:
                left = char_next_index[char]
            ans = max(ans, right - left + 1)
            char_next_index[char] = right + 1
        return ans



            
            
        



        