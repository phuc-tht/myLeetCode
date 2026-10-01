class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s: return("")
        if len(s) == 1: return(s)

        s_ini = s
        s = "@#" + "#".join(s) + "#$"

        radius = [0] * len(s)
        center = right_bound = 0

        for i in range(1, len(s) - 1):
            i_mirror = 2 * center - i
            if i < right_bound:
                radius[i] = min(right_bound - i, radius[i_mirror])
            while s[i + radius[i] + 1] == s[i - radius[i] - 1]:
                radius[i] += 1
            if i + radius[i] > right_bound:
                center = i
                rght_bound = i + radius[i]
                
        max_len = max(radius)
        center_index = radius.index(max(radius))
        start = (center_index - max_len) // 2
        return s_ini[start: start + max_len]