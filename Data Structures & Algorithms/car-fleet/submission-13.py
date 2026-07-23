class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed), reverse = True)
        stack = []
        for position, speed in pairs:
            time = (target - position) / speed
            if stack and time <= stack[-1]:
                continue
            stack.append(time)
        return len(stack)