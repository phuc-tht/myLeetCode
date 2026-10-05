class Solution:
    def reverse(self, x: int) -> int:
        ans = ""
        abs_x = abs(x)
        for num in str(abs_x):
            ans = num + ans
        if x < 0: ans = str(-int(ans))
        if - 2 ** 31 > int(ans) or 2 ** 31 - 1 < int(ans):
            return(0) 
        else:
            return(int(ans))