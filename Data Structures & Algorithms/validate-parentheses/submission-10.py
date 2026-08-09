class Solution:
    def isValid(self, s: str) -> bool:
        stk = []

        for sym in s:
            if sym in '[({':
                stk.append(sym)

            if not stk: return False

            print(stk)
            if sym == '}' and stk.pop() != '{':
                return False
            elif sym == ')' and stk.pop() != '(':
                return False
            elif sym == ']' and stk.pop() != '[':
                return False
        return len(stk) == 0
            