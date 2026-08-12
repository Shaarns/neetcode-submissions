class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed))
        #[0, 1, 4, 7]
        #[1, 2, 2, 1]
        stack = []

        for p, spd in reversed(cars):
            time = (target - p) / spd

            stack.append(time)

            if len(stack) >=2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)




