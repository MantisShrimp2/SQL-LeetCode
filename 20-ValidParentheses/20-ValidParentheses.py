# Last updated: 3/5/2026, 4:16:00 PM
class Solution(object):
    def isValid(self, s):
        stack = []
        
        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        } # it will compile from left to right then now 
        
        for ch in s:# push to stack 
            if ch in "({[":
                stack.append(ch)
            else:
                if not stack:
                    return False
                
                top = stack.pop()#storing the top bracket so that we can compare it with thecurrent closing bracket 
                
                if pairs[ch] != top: 
                    return False
        
        return len(stack) == 0