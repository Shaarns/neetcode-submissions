class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        pairs = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        for sym in s:
            if sym in pairs:
                if not stk or stk.pop() != pairs[sym]:
                    return False
                
            else:
                stk.append(sym)
            
        return len(stk) == 0
            