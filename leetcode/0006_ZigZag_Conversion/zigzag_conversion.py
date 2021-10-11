# solution 1:
class Solution1:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        L = [''] * numRows
        index, step = 0, 1

        for x in s:
            L[index] += x
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step

        return ''.join(L)

# Solution 2
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # If we have only one row then we can return the string as it is
        if numRows < 2:
            return s
        # We will create an empty string for each row and then fill each element in each row
        # from row = 0 to row = numRows-1, if we reach bottom (i.e. row = numRows-1)
        # then we move up. Similarly if we reach top, we change direction and move down
        # Finally after filling up all the four rows we join them row0 + row1 +.. numRows
        row = 0
        result = [""]*numRows
        for character in s:
            if row == 0:
                move_down = True
            elif row == numRows-1:
                move_down = False
            result[row] += character
            row = (row+1) if move_down else row-1

        return "".join(result)

if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.convert("PAYPALISHIRING", 3))