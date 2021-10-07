# Solution 1
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs or len(strs) == 0:
            return ""
        
        strs.sort()
        
        res = ""
        pair = zip(strs[0], strs[-1])
        for x, y in pair:
            if x == y:
                res += x
            else:
                break
        return res
        

# Solution 2
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l = list(zip(*strs))
        prefix = ""
        for i in l:
            if len(set(i))==1:
                prefix += i[0]
            else:
                break
        return prefix