# [8. String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi/)

## Problems:
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function). <br>

The algorithm for myAtoi(string s) is as follows: <br>

1. Read in and ignore any leading whitespace.
Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
2. Read in next the characters until the next non-digit charcter or the end of the input is reached. The rest of the string is ignored.
3. Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
4. If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
5. Return the integer as the final result.

Note: <br>
* Only the space character ' ' is considered a whitespace character.
* Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.
 

### Example 1:
Input: s = "42" <br>
Output: 42 <br>
Explanation: The underlined characters are what is read in, the caret is the current reader position. <br>
Step 1: "42" (no characters read because there is no leading whitespace) <br>
         ^ <br>
Step 2: "42" (no characters read because there is neither a '-' nor '+') <br>
         ^ <br>
Step 3: "42" ("42" is read in) <br>
           ^ <br>
The parsed integer is 42. <br>
Since 42 is in the range [-231, 231 - 1], the final result is 42. <br>

### Example 2:
Input: s = "   -42" <br>
Output: -42 <br>
Explanation: <br>
Step 1: "   -42" (leading whitespace is read and ignored) <br>
            ^ <br>
Step 2: "   -42" ('-' is read, so the result should be negative) <br>
             ^ <br>
Step 3: "   -42" ("42" is read in) <br>
               ^ <br>
The parsed integer is -42. <br>
Since -42 is in the range [-231, 231 - 1], the final result is -42. <br>

### Example 3:
Input: s = "4193 with words" <br>
Output: 4193 <br>
Explanation: <br>
Step 1: "4193 with words" (no characters read because there is no leading whitespace) <br>
         ^ <br>
Step 2: "4193 with words" (no characters read because there is neither a '-' nor '+') <br>
         ^ <br>
Step 3: "4193 with words" ("4193" is read in; reading stops because the next character is a non-digit) <br>
             ^ <br>
The parsed integer is 4193. <br>
Since 4193 is in the range [-231, 231 - 1], the final result is 4193. <br>

### Example 4:
Input: s = "words and 987" <br>
Output: 0 <br>
Explanation: <br>
Step 1: "words and 987" (no characters read because there is no leading whitespace) <br>
         ^ <br>
Step 2: "words and 987" (no characters read because there is neither a '-' nor '+') <br>
         ^ <br>
Step 3: "words and 987" (reading stops immediately because there is a non-digit 'w')
         ^ <br>
The parsed integer is 0 because no digits were read. <br>
Since 0 is in the range [-231, 231 - 1], the final result is 0. <br>

### Example 5:
Input: s = "-91283472332" <br>
Output: -2147483648 <br>
Explanation: <br>
Step 1: "-91283472332" (no characters read because there is no leading whitespace) <br>
         ^ <br>
Step 2: "-91283472332" ('-' is read, so the <br> result should be negative) <br>
          ^ <br>
Step 3: "-91283472332" ("91283472332" is read in) <br>
                     ^ <br>
The parsed integer is -91283472332. <br>
Since -91283472332 is less than the lower bound of the range [-231, 231 - 1], the final result is clamped to -231 = -2147483648. <br>


### Constraints:
* 0 <= s.length <= 200
* s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.


