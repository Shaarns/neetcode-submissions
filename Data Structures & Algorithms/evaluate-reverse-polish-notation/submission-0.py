class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = ['*', '/', "+", '-']
        stk = []

        for token in tokens:
            if token not in operands:
                stk.append(token)
            else:
                num1 = int(stk.pop())
                num2 = int(stk.pop())
                
                if token == '+':
                    output = num2 + num1
                elif token == '-':
                    output = num2 - num1
                elif token == '*':
                    output = num2 * num1
                else: 
                    output = int(num2 / num1)

                stk.append(output)

        return int(stk.pop())