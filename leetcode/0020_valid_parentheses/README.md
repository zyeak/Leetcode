# [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)

## Problems:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.<br>

An input string is valid if: <br>
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

### Example 1:
Input: s = "()" <br>
Output: true <br>

### Example 2:
Input: s = "()[]{}" <br>
Output: true <br>

### Example 3:
Input: s = "(]" <br>
Output: false <br>

### Example 4:
Input: s = "([)]" <br>
Output: false <br>

### Example 5:
Input: s = "{[]}" <br>
Output: true <br>

### Constraints:
* 1 <= s.length <= 104
* s consists of parentheses only '()[]{}'.