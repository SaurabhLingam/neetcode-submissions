class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for ch in tokens:
            try:
                stack.append(int(ch))
            except:
                right_operand = stack.pop()
                left_operand = stack.pop()
                if ch == "+":
                    stack.append(left_operand + right_operand)                
                elif ch == "-":
                    stack.append(left_operand - right_operand)                
                elif ch == "*":
                    stack.append(left_operand * right_operand)                
                elif ch == "/":
                    stack.append(int(left_operand / right_operand))
        return int(stack[0])                
