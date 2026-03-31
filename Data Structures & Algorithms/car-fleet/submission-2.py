class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(list(zip(position,speed)))

        stack = []

        for position,speed in cars[::-1]:
            time = (target - position)/speed
            stack.append(time)

            if len(stack)>= 2 and stack[-1] <= stack[-2]:
                    #[3,4.5,10,3]
                    #[3,10]
                    stack.pop()

        return len(stack)





              



        





