class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        speed_dict = {}
        for i in range(len(position)):
            speed_dict[position[i]] = speed[i]

        #[0, 1, 4, 7]
        #[1, 2, 2, 1]
        position.sort()
        stack = []

        for p in range(len(position)-1, -1, -1):
            spd = speed_dict[position[p]]
            time = (target - position[p]) / spd

            stack.append(time)

            if len(stack) >=2:
                tm2 = stack[-1]
                tm1 = stack[-2]

                if tm1 >= tm2:
                    stack.pop()

        return len(stack)




