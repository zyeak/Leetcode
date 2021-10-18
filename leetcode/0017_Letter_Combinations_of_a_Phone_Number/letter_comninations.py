# Solution1:
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        key_dic = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        result = [''] if digits else []
        for d in digits:
            result = [p+q for p in result for q in key_dic[d]]
            
        return result

# Solution2: backtracking solution
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        key_dic = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        
        if not digits:
            return []
        
        result = []
        self.dfs(key_dic, digits, '', result)
        return result
        
    def dfs(self, key_dic, digits, path, result):
        if not digits:
            result.append(path)
            return
        for d in key_dic[digits[0]]:
            self.dfs(key_dic, digits[1:], path+d, result)
        