class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {")": "(", "}": "{", "]": "["}
        for ch in s:
            if ch in "{[(":
                stack.append(ch)
            elif ch in matching:
                
                if not stack or stack[-1] != matching[ch]:
                    return False
                stack.pop()

        return len(stack) == 0