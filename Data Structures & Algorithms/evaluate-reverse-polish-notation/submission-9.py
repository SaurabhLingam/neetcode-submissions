class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            try:
                stack.append(int(token))
            except:
                right_operand = stack.pop()
                left_operand = stack.pop()
                if token == "+":
                    stack.append(left_operand + right_operand)
                elif token == "-":
                    stack.append(left_operand - right_operand)
                if token == "*":
                    stack.append(left_operand * right_operand)
                if token == "/":
                    stack.append(int(left_operand / right_operand));
        return stack[0]
                