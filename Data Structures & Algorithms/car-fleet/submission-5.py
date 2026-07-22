class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed), reverse=True)
        stack = []
        for position, speed in pairs:
            print(position)
            print(speed)
            time = (target - position) / speed
            print(time)
            if stack and time <= stack[-1]:
                continue
            stack.append(time)
            print("stack appended", time)
        return len(stack)