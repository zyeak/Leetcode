# Solution 1
class Solution:
    def isValid(self, s: str) -> bool:
        
        dic = {")":"(", "]":"[", "}":"{"}
        stack = []
        
        for c in s :
            if c in ["(", "[", "{"]:
                stack.append(c)
            else:
                if not stack or dic[c] != stack[-1]:
                    return False
                stack.pop()
        return len(stack) == 0

# Solution 2
class Solution:
    def isValid(self, s: str) -> bool:
        while len(s)>0:
            l = len(s)
            s = s.replace('()', '').replace('[]','').replace('{}','')
            if l == len(s): return False
        return True