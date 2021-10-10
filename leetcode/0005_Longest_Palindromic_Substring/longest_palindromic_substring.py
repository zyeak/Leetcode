# Solution 1:  
class Solution(object):
    def longestPalindrome(self, s):
        result = ""
        for i in range(len(s)):
            # odd case, like 'aba'
            tmp = self.palindromeAt(s, i, i)
            if len(tmp) > len(result):
                result = tmp
            # even case, like 'abba'
            tmp = self.palindromeAt(s, i, i+1)
            if len(tmp) > len(result):
                result = tmp
        return result
    # get the longest palindrome, l, r are the middle indexes from inner to outer           
    def palindromeAt(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r] 
if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.longestPalindrome("abcbe"))