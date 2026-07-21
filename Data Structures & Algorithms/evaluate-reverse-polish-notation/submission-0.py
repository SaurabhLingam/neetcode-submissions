class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for ch in tokens:
            try:
                stack.append(int(ch))
            except:
                operation = ch
                right_operand = stack.pop()
                left_operand = stack.pop()
                if operation == "+":
                    stack.append(left_operand + right_operand)
                elif operation == "-":
                    stack.append(left_operand - right_operand)
                elif operation == "*":
                    stack.append(left_operand * right_operand)
                elif operation == "/":
                    stack.append(int(left_operand / right_operand))
        return stack[0]
                
