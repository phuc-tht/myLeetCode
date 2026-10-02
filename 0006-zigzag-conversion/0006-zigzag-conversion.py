class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        wid = 0
        if numRows == 1:
            return(s)
        if n % (2 * numRows - 2) <= numRows:
            wid = (n // (2 * numRows - 2)) * (numRows - 1) + 1
        else:
            wid = (n // (2 * numRows - 2)) * (numRows - 1) + n % (2 * numRows - 2) - numRows + 1
        table = [["" for x in range(wid)] for y in range(numRows)]
        i = j = 0
        while s:
            table[i][j] = s[0]
            s = s[1:]
            if i == 0 or table[i - 1][j] and i < numRows - 1:
                i += 1
            else:
                i -= 1; j += 1
        return("".join(string for cell in table for string in cell))


