class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s: return(0)
        sign = 1
        match s[0]:
            case "-":
                sign = -1
                s = s[1:]
            case "+":
                sign = 1
                s = s[1:]
        if not s: return(0)
        num_list = ["0", "1", "2", "3", "4", "5","6", "7", "8", "9"]
        if s[0] not in num_list:
            return(0)
        ans = 0
        factor = 1    
        for char in reversed(s):
            match char:
                case "0": 
                    factor *= 10
                case "1": 
                    ans += 1 * factor
                    factor *= 10
                case "2": 
                    ans += 2 * factor
                    factor *= 10
                case "3": 
                    ans += 3 * factor
                    factor *= 10
                case "4": 
                    ans += 4 * factor
                    factor *= 10
                case "5": 
                    ans += 5 * factor
                    factor *= 10
                case "6": 
                    ans += 6 * factor
                    factor *= 10
                case "7": 
                    ans += 7 * factor
                    factor *= 10
                case "8": 
                    ans += 8 * factor
                    factor *= 10
                case "9": 
                    ans += 9 * factor
                    factor *= 10
                case _:
                    ans = 0
                    factor = 1
        ans *= sign
        if ans < -2 ** 31: return(-2 ** 31)
        if ans > 2 ** 31 - 1: return(2 ** 31 - 1)
        return(ans)